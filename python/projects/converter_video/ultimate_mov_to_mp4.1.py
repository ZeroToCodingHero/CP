#!/usr/bin/env python3
"""
ULTIMATE UNIVERSAL VIDEO BATCH CONVERTER (2025)
Converts ANY video format → MP4 (or HEVC/AV1)
Supports: .mov .mkv .avi .wmv .flv .webm .m4v .mpg .ts .mts .vob .3gp .ogv etc.
"""

import os
import sys
import ffmpeg
import hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import platform
import subprocess

# ========================== CONFIG ==========================
TARGET_FORMAT = "mp4"           # Change to "mp4" or "mkv"
VIDEO_CODEC = "h264"            # "h264" (best compatibility), "hevc" (smaller), "av1" (future)
CRF = 20                        # 18–24 for H.264/HEVC (lower = better), 24–30 for AV1
PRESET = "slow"                 # slow, medium, fast, veryfast
USE_HEVC = (VIDEO_CODEC == "hevc")
USE_AV1 = (VIDEO_CODEC == "av1")
DELETE_ORIGINAL = False
MOVE_TO_TRASH = True
MAX_WORKERS = os.cpu_count() * 2
# ===========================================================

# Common video extensions (add more if needed)
VIDEO_EXTS = {
    '.mov', '.mkv', '.avi', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg',
    '.mp4', '.ts', '.mts', '.m2ts', '.vob', '.3gp', '.3g2', '.ogv', '.divx',
    '.hevc', '.h265', '.av1', '.m2v', '.m4b'
}

def get_best_encoder():
    system = platform.system()
    if USE_AV1:
        return "libsvtav1", ["-crf", str(CRF), "-preset", "4"]
    if USE_HEVC:
        if system == "Darwin":
            return "hevc_videotoolbox", ["-q:v", "50"]
        elif "nvidia-smi" in subprocess.getoutput("which nvidia-smi || true"):
            return "hevc_nvenc", ["-cq", "22"]
        else:
            return "libx265", ["-crf", str(CRF), "-preset", PRESET]
    else:
        if system == "Darwin":
            return "h264_videotoolbox", ["-q:v", "50"]
        elif "nvidia-smi" in subprocess.getoutput("which nvidia-smi || true"):
            return "h264_nvenc", ["-cq", "21"]
        else:
            return "libx264", ["-crf", str(CRF), "-preset", PRESET]

def needs_transcode(input_path):
    """Check if file can be remuxed only (instant) or needs re-encode"""
    try:
        probe = ffmpeg.probe(input_path)
        vstream = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        codec = vstream['codec_name'].lower()
        if TARGET_FORMAT == "mp4":
            if codec in ['h264', 'hevc', 'mpeg4'] and codec != 'av1':
                return False  # Can remux only
        return True
    except:
        return True

def convert_video(input_path: Path):
    output_path = input_path.with_suffix(f'.{TARGET_FORMAT}')

    if output_path.exists():
        return True, "skip_exists"

    # Instant remux if possible (zero quality loss, lightning fast)
    if not needs_transcode(str(input_path)) and TARGET_FORMAT == "mp4":
        try:
            stream = ffmpeg.input(str(input_path))
            stream = ffmpeg.output(stream, str(output_path), c='copy', movflags='+faststart')
            ffmpeg.run(stream, overwrite_output=True, quiet=True)
            return True, "remuxed"
        except:
            pass  # Fall back to full encode

    encoder, extra_args = get_best_encoder()
    codec_name = "hevc" if USE_HEVC else "av1" if USE_AV1 else "libx264"

    try:
        stream = ffmpeg.input(str(input_path))
        args = {
            'c:v': encoder,
            'c:a': 'aac' if TARGET_FORMAT == "mp4" else 'copy',
            'b:a': '192k' if TARGET_FORMAT == "mp4" else None,
            'c:s': 'mov_text' if TARGET_FORMAT == "mp4" else 'copy',
            'movflags': '+faststart',
            'pix_fmt': 'yuv420p',
        }
        if extra_args:
            for i in range(0, len(extra_args), 2):
                args[extra_args[i]] = extra_args[i+1]

        stream = ffmpeg.output(stream, str(output_path), **{k: v for k, v in args.items() if v})
        ffmpeg.run(stream, overwrite_output=True, quiet=True)
        return True, f"encoded_{codec_name}"
    except Exception as e:
        return False, f"error: {str(e)[:100]}"

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else input("Folder path: ").strip('"\''))
    if not root.exists():
        print("Folder not found!")
        return

    print(f"Scanning for video files in: {root}")
    files = []
    for ext in VIDEO_EXTS:
        files.extend(root.rglob(f"*{ext}"))
        files.extend(root.rglob(f"*{ext.upper()}"))

    files = [f for f in files if f.is_file() and f.suffix.lower() != f'.{TARGET_FORMAT}']
    files = list(dict.fromkeys(files))  # dedupe

    if not files:
        print("No videos found.")
        return

    print(f"Found {len(files)} videos → converting to .{TARGET_FORMAT} ({VIDEO_CODEC.upper()})")
    print(f"Encoder: {get_best_encoder()[0]} | CRF: {CRF} | Preset: {PRESET}")
    print(f"Remux when possible: {'Yes' if TARGET_FORMAT == 'mp4' else 'No'}")
    print("-" * 70)

    results = {"converted": 0, "remuxed": 0, "skipped": 0, "failed": 0}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(convert_video, f): f for f in files}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Converting", unit="file"):
            path = futures[future]
            success, msg = future.result()
            if success:
                if "remuxed" in msg:
                    results["remuxed"] += 1
                    tqdm.write(f"Remuxed: {path.name}")
                elif "encoded" in msg:
                    results["converted"] += 1
                    tqdm.write(f"Converted: {path.name}")
                else:
                    results["skipped"] += 1
                # Delete/trash original
                if (DELETE_ORIGINAL or MOVE_TO_TRASH) and "skip" not in msg:
                    try:
                        from send2trash import send2trash
                        send2trash(str(path))
                        tqdm.write(f"Trashed: {path.name}")
                    except:
                        if DELETE_ORIGINAL:
                            path.unlink()
            else:
                results["failed"] += 1
                tqdm.write(f"Failed: {path.name} → {msg}")

    print("\n" + "="*60)
    print("UNIVERSAL BATCH CONVERSION COMPLETE")
    print(f"Remuxed (instant):  {results['remuxed']}")
    print(f"Encoded:            {results['converted']}")
    print(f"Skipped:            {results['skipped']}")
    print(f"Failed:             {results['failed']}")
    print("="*60)

if __name__ == "__main__":
    try:
        from tqdm import tqdm
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ffmpeg-python", "tqdm", "send2trash"])
        print("Dependencies installed. Run again!")
    else:
        main()