#!/usr/bin/env python3
"""
Ultimate MOV → MP4 Batch Converter (2025)
- Recursive
- High-quality CRF encoding
- Hardware acceleration (auto-detect)
- Progress bar + smart skip
- Safe delete / trash originals
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

# -------------------------- CONFIG --------------------------
CRF = 18                    # 17-23: 18 = visually lossless, 23 = excellent, 28 = smaller
PRESET = "slow"             # slow = best compression, medium/fast/veryfast for speed
TUNE = None                 # e.g., "film", "animation", None
DELETE_ORIGINAL = False     # Set to True to delete .mov after success
MOVE_TO_TRASH = True        # Safer: move to system trash instead of permanent delete
MAX_WORKERS = os.cpu_count() * 2  # Adjust if you want to limit GPU/CPU usage
# ------------------------------------------------------------

def get_hardware_encoder():
    """Auto-detect best available hardware encoder"""
    system = platform.system()
    machine = platform.machine()

    if system == "Darwin":  # macOS
        return "h264_videotoolbox", ["-q:v", "50"]  # 0-100, lower = better
    elif subprocess.run(["which", "nvidia-smi"], capture_output=True).returncode == 0:
        return "h264_nvenc", ["-cq", str(19)]  # 0-51, lower = better
    elif "AMD" in subprocess.getoutput("lspci | grep VGA 2>/dev/null || true"):
        return "h264_amf", ["-quality", "quality"]
    elif "Intel" in subprocess.getoutput("lspci | grep VGA 2>/dev/null || true"):
        return "h264_qsv", ["-global_quality", str(18)]
    else:
        return "libx264", ["-crf", str(CRF), "-preset", PRESET]

def file_hash(filepath, chunk_size=65536):
    """Fast hash to detect if file was already converted perfectly"""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def trash_file(path: Path):
    """Move file to system trash (cross-platform)"""
    try:
        from send2trash import send2trash
        send2trash(str(path))
        return True
    except ImportError:
        print("send2trash not installed. Install with: pip install send2trash")
        return False
    except Exception as e:
        print(f"Failed to trash {path}: {e}")
        return False

def convert_single_file(mov_path: Path, dry_run=False):
    mp4_path = mov_path.with_suffix('.mp4')

    # Skip if already exists and hash matches (perfect re-encode skip)
    if mp4_path.exists():
        if file_hash(mov_path) == file_hash(mp4_path):
            return True, "identical_skip"
        # Optional: skip any existing mp4
        # return True, "exists_skip"

    if dry_run:
        return True, "dry_run"

    encoder, extra_args = get_hardware_encoder()

    try:
        stream = ffmpeg.input(str(mov_path))

        # Common high-quality args
        args = {
            'c:v': encoder,
            'c:a': 'aac',
            'b:a': '192k',
            'movflags': '+faststart',  # Web-optimized
            'pix_fmt': 'yuv420p',      # Maximum compatibility
        }

        # Add encoder-specific quality settings
        if encoder == "libx264":
            args.update({
                'crf': CRF,
                'preset': PRESET,
            })
            if TUNE:
                args['tune'] = TUNE
        else:
            args.update(dict([extra_args]))  # e.g., -cq 19 for nvenc

        stream = ffmpeg.output(stream, str(mp4_path), **args)
        ffmpeg.run(stream, overwrite_output=True, quiet=True, cmd='ffmpeg')

        # Post-conversion safety check
        if mp4_path.stat().st_size < 1024:
            mp4_path.unlink(missing_ok=True)
            return False, "failed_empty"

        return True, "converted"

    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        return False, f"ffmpeg_error: {error_msg.splitlines()[0] if error_msg else 'unknown'}"
    except Exception as e:
        return False, f"error: {str(e)}"

def main():
    if len(sys.argv) > 1:
        root_dir = Path(sys.argv[1])
    else:
        root_dir = Path(input("Enter folder path (drag & drop works): ").strip('"\''))

    if not root_dir.exists():
        print("Folder not found!")
        return

    print(f"Scanning recursively in: {root_dir.resolve()}")
    mov_files = [p for p in root_dir.rglob("*.mov") if p.is_file()]
    mov_files += [p for p in root_dir.rglob("*.MOV") if p.is_file()]

    if not mov_files:
        print("No .mov files found.")
        return

    print(f"Found {len(mov_files)} .mov files")
    print(f"Using encoder: {get_hardware_encoder()[0]} (CRF≈{CRF})")
    print(f"Threads: {MAX_WORKERS}")
    print(f"Delete original: {'Trash' if MOVE_TO_TRASH else 'Permanent' if DELETE_ORIGINAL else 'No'}")
    print("-" * 60)

    # Dry run first
    print("Dry run: checking what would be converted...")
    to_convert = []
    for mov in mov_files:
        success, msg = convert_single_file(mov, dry_run=True)
        if "skip" not in msg:
            to_convert.append(mov)

    if not to_convert:
        print("All files already perfectly converted!")
        return

    print(f"{len(to_convert)} files need conversion. Starting...\n")

    # Real conversion with progress bar
    results = {
        "converted": 0,
        "skipped": 0,
        "failed": 0
    }

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(convert_single_file, mov): mov for mov in to_convert}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Converting", unit="file"):
            mov_path = futures[future]
            success, msg = future.result()

            if "skip" in msg:
                results["skipped"] += 1
            elif success:
                results["converted"] += 1
                tqdm.write(f"Converted: {mov_path.name}")

                # Safely remove original
                if DELETE_ORIGINAL or MOVE_TO_TRASH:
                    if MOVE_TO_TRASH and trash_file(mov_path):
                        tqdm.write(f"Trashed: {mov_path.name}")
                    elif DELETE_ORIGINAL:
                        try:
                            mov_path.unlink()
                            tqdm.write(f"Deleted: {mov_path.name}")
                        except:
                            pass
            else:
                results["failed"] += 1
                tqdm.write(f"Failed: {mov_path.name} → {msg}")

    # Final report
    print("\n" + "="*60)
    print("BATCH CONVERSION COMPLETE")
    print(f"Converted: {results['converted']}")
    print(f"Skipped:   {results['skipped']}")
    print(f"Failed:    {results['failed']}")
    print("="*60)

if __name__ == "__main__":
    # Auto-install missing deps on first run (optional)
    try:
        from tqdm import tqdm
        import ffmpeg
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ffmpeg-python", "tqdm", "send2trash"])
        print("Installed! Run the script again.")
    else:
        main()