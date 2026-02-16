# Quansheng UV-K5 driver (c) 2023 Jacek Lipkowski <sq5bpf@lipkowski.org>
# Adapted For UV-K5 EGZUMER custom software By EGZUMER, JOC2
#
# This is a CHIRP driver (memory programmer) for the Quansheng UV-K5 / UV-K6
# radios running the popular EGZUMER custom firmware.

import struct
import logging
import wx
from chirp import chirp_common, directory, bitwise, memmap, errors, util
from chirp.settings import RadioSetting, RadioSettingGroup, \
    RadioSettingValueBoolean, RadioSettingValueList, \
    RadioSettingValueInteger, RadioSettingValueString, \
    RadioSettings, InvalidValueError

LOG = logging.getLogger(__name__)

# ────────────────────────────────────────────────
#  Debug flags (useful during driver development)
# ────────────────────────────────────────────────
DEBUG_SHOW_OBFUSCATED_COMMANDS = False    # show XOR-obfuscated packets
DEBUG_SHOW_MEMORY_ACTIONS      = False    # show memory read/write blocks

# Driver identification shown in CHIRP
DRIVER_VERSION = "Quansheng UV-K5/K6/5R driver (c) egzumer"

# ────────────────────────────────────────────────
#          MEMORY LAYOUT DEFINITION
# ────────────────────────────────────────────────
# This is the most important part — it tells CHIRP how the radio's EEPROM
# is structured (which bytes mean what setting).
#
MEM_FORMAT = """
//#seekto 0x0000;           // beginning of channel memory
struct {
  ul32 freq;                // RX frequency × 10 Hz
  ul32 offset;              // repeater offset × 10 Hz
  u8 rxcode;                // RX CTCSS/DCS code index
  u8 txcode;                // TX CTCSS/DCS code index
  u8 txcodeflag:4,          // TX code type (none/tone/DCS/R-DCS)
     rxcodeflag:4;          // RX code type
  u8 modulation:4,          // modulation type
     offsetDir:4;           // + / - / none
  u8 __UNUSED1:3,
     busyChLockout:1,       // Busy Channel Lockout (BCLO)
     txpower:2,             // power level (low/med/high)
     bandwidth:1,           // wide / narrow
     freq_reverse:1;        // frequency reverse (cross-band like)
  u8 __UNUSED2:4,
     dtmf_pttid:3,          // PTT-ID mode
     dtmf_decode:1;         // DTMF decode enable
  u8 step;                  // step index (2.5k, 5k, 6.25k, ...)
  u8 scrambler;             // voice scrambler setting
} channel[214];             // 200 normal + 14 special (VFOs)

// channel attributes (scan list membership, compander, band, empty flag)
#seekto 0xd60;
struct {
  u8 is_scanlist1:1,
     is_scanlist2:1,
     compander:2,
     is_free:1,             // 1 = channel is empty
     band:3;                // which band this channel belongs to
} ch_attr[200];

// FM radio presets
#seekto 0xe40;
ul16 fmfreq[20];            // 20 × FM preset frequencies × 10 kHz

// Global settings
#seekto 0xe70;
u8 call_channel;            // one-touch call channel number
u8 squelch;
u8 max_talk_time;           // TOT (time-out timer)
u8 noaa_autoscan;
u8 key_lock;
u8 vox_switch;
u8 vox_level;
u8 mic_gain;
u8 backlight_min:4,
   backlight_max:4;
u8 channel_display_mode;
u8 crossband;
u8 battery_save;
u8 dual_watch;
u8 backlight_time;
u8 ste;                     // squelch tail elimination
u8 freq_mode_allowed;       // allow VFO/frequency mode?

// Currently active channels on each side
#seekto 0xe80;
u8 ScreenChannel_A;
u8 MrChannel_A;
u8 FreqChannel_A;
u8 ScreenChannel_B;
u8 MrChannel_B;
u8 FreqChannel_B;
u8 NoaaChannel_A;
u8 NoaaChannel_B;

// Key behavior
#seekto 0xe90;
u8 keyM_longpress_action:7,
   button_beep:1;
u8 key1_shortpress_action;
u8 key1_longpress_action;
u8 key2_shortpress_action;
u8 key2_longpress_action;
u8 scan_resume_mode;
u8 auto_keypad_lock;
u8 power_on_dispmode;
ul32 password;              // 6-digit power-on password (or 0xFFFFFFFF = off)

// Voice prompts, S-meter calibration
#seekto 0xea0;
u8 voice;
u8 s0_level;                // S-meter calibration S0
u8 s9_level;                // S-meter calibration S9

// Other miscellaneous settings
#seekto 0xea8;
u8 alarm_mode;
u8 roger_beep;
u8 rp_ste;                  // repeater tail elimination delay
u8 TX_VFO;                  // which VFO is used for TX (A/B)
u8 Battery_type;

// Welcome message / logo
#seekto 0xeb0;
char logo_line1[16];
char logo_line2[16];

// DTMF settings block
#seekto 0xed0;
struct {
    u8 side_tone;
    char separate_code;
    char group_call_code;
    u8 decode_response;
    u8 auto_reset_time;
    u8 preload_time;
    u8 first_code_persist_time;
    u8 hash_persist_time;
    u8 code_persist_time;
    u8 code_interval_time;
    u8 permit_remote_kill;
    #seekto 0xee0;
    char local_code[3];
    #seek 5;
    char kill_code[5];
    #seek 3;
    char revive_code[5];
    #seek 3;
    char up_code[16];
    char down_code[16];
} dtmf;

// Scan list priority settings
#seekto 0xf18;
u8 slDef;
u8 sl1PriorEnab;
u8 sl1PriorCh1;
u8 sl1PriorCh2;
u8 sl2PriorEnab;
u8 sl2PriorCh1;
u8 sl2PriorCh2;

// Hidden / factory / unlock flags
#seekto 0xf40;
u8 int_flock;               // frequency lock mode
u8 int_350tx;               // TX 350–400 unlocked
u8 int_KILLED;              // radio is DTMF-killed
u8 int_200tx;
u8 int_500tx;
u8 int_350en;
u8 int_scren;               // scrambler enabled
u8 backlight_on_TX_RX:2,
   AM_fix:1,
   mic_bar:1,
   battery_text:2,
   live_DTMF_decoder:1,
   unknown:1;

// Channel names (alphanumeric tags)
#seekto 0xf50;
struct {
    char name[16];
} channelname[200];

// DTMF contact list (ANI / speed dial like)
#seekto 0x1c00;
struct {
    char name[8];
    char number[3];
    #seek 5;
} dtmfcontact[16];

// ────────────────────────────────────────────────
//        C A L I B R A T I O N   D A T A
// ────────────────────────────────────────────────
#seekto 0x1E00;
struct {
    // Squelch calibration tables for different bands
    struct { ... } sqlBand4_7;
    struct { ... } sqlBand1_3;

    // RSSI bar graph calibration points
    struct { ul16 level1, level2, level4, level6; } rssiLevelsBands3_7;
    struct { ul16 level1, level2, level4, level6; } rssiLevelsBands1_2;

    // TX power calibration curves (low/mid/hi) for each band
    struct { struct { u8 lower,center,upper; } low,mid,hi; #seek 7; } txp[7];

    // Battery voltage levels
    #seekto 0x1F40;
    ul16 batLvl[6];

    // VOX thresholds
    #seekto 0x1F50;
    ul16 vox1Thr[10];
    #seekto 0x1F68;
    ul16 vox0Thr[10];

    // Microphone gain steps
    #seekto 0x1F80;
    u8 micLevel[5];

    // Crystal frequency offset & audio gains
    #seekto 0x1F88;
    il16 xtalFreqLow;
    u8 volumeGain;
    u8 dacGain;
} cal;

// Feature flags compiled into the firmware
#seekto 0x1FF0;
struct {
    u8 ENABLE_DTMF_CALLING      :1,
       ENABLE_PWRON_PASSWORD    :1,
       ENABLE_TX1750            :1,
       ENABLE_ALARM             :1,
       ENABLE_VOX               :1,
       ENABLE_VOICE             :1,
       ENABLE_NOAA              :1,
       ENABLE_FMRADIO           :1;
    u8 __UNUSED                 :3,
       ENABLE_AM_FIX            :1,
       ENABLE_BLMIN_TMP_OFF     :1,
       ENABLE_RAW_DEMODULATORS  :1,
       ENABLE_WIDE_RX           :1,
       ENABLE_FLASHLIGHT        :1;
} BUILD_OPTIONS;
"""

# ────────────────────────────────────────────────
#               C O N S T A N T S
# ────────────────────────────────────────────────

# Offset direction flags
FLAGS1_OFFSET_NONE   = 0b00
FLAGS1_OFFSET_MINUS  = 0b10
FLAGS1_OFFSET_PLUS   = 0b01

# Power levels (shown in CHIRP UI)
UVK5_POWER_LEVELS = [
    chirp_common.PowerLevel("Low",  watts=1.50),
    chirp_common.PowerLevel("Med",  watts=3.00),
    chirp_common.PowerLevel("High", watts=5.00),
]

# Voice scrambler tones
SCRAMBLER_LIST = ["OFF", "2600Hz", "2700Hz", ..., "3500Hz"]

# Many other lookup tables follow (CTCSS, DCS, steps, backlight times, etc.)
# They are omitted here for brevity

# ────────────────────────────────────────────────
#         Obfuscation & Communication Layer
# ────────────────────────────────────────────────

def xorarr(data: bytes):
    """ XOR obfuscation used in every command and response """
    # rotating key table
    tbl = [22, 108, 20, 230, 46, 145, 13, 64, 33, 53, 213, 64, 19, 3, 233, 128]
    ret = b""
    idx = 0
    for byte in data:
        ret += bytes([byte ^ tbl[idx]])
        idx = (idx + 1) % len(tbl)
    return ret


def calculate_crc16_xmodem(data: bytes):
    """ CRC-16/XMODEM used only in one direction (extra obfuscation) """
    poly = 0x1021
    crc = 0x0
    for byte in data:
        crc = crc ^ (byte << 8)
        for _ in range(8):
            crc = crc << 1
            if crc & 0x10000:
                crc = (crc ^ poly) & 0xFFFF
    return crc & 0xFFFF


def _send_command(serport, data: bytes):
    """ Send obfuscated command packet to radio """
    # Calculate CRC → XOR → wrap with magic bytes AB CD ... DC BA
    ...


def _receive_reply(serport):
    """ Receive & de-obfuscate reply from radio """
    ...


# ────────────────────────────────────────────────
#         Main download / upload routines
# ────────────────────────────────────────────────

def do_download(radio):
    """ Download entire EEPROM image from radio """
    ...


def do_upload(radio):
    """ Upload modified EEPROM image back to radio """
    ...


# ────────────────────────────────────────────────
#           The actual radio driver class
# ────────────────────────────────────────────────

@directory.register
class UVK5Radio(chirp_common.CloneModeRadio):
    """Quansheng UV-K5 / UV-K6 (EGZUMER firmware)"""

    VENDOR = "Quansheng"
    MODEL = "UV-K5 (egzumer)"
    BAUD_RATE = 38400

    # Called when user clicks "Download from Radio"
    def sync_in(self):
        self._mmap = do_download(self)
        self.process_mmap()

    # Called when user clicks "Upload to Radio"
    def sync_out(self):
        do_upload(self)

    # Parse raw bytes into structured object
    def process_mmap(self):
        self._memobj = bitwise.parse(MEM_FORMAT, self._mmap)

    # ─── Memory read/write ────────────────────────────────────────

    def get_memory(self, number):
        """ Convert low-level memory → CHIRP Memory object """
        ...

    def set_memory(self, memory):
        """ Convert CHIRP Memory object → low-level memory """
        ...

    # ─── Settings UI tree ─────────────────────────────────────────

    def get_settings(self):
        """ Build the whole Settings tab (very long function) """
        ...

    def set_settings(self, settings):
        """ Write changed settings back to memory map """
        ...

    # Validation, band checks, tone conversion, etc.
    ...
