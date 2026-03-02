import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def parse_args():
    parser = argparse.ArgumentParser(description="Publish SBS DSW update payload and manifest.")
    parser.add_argument("--exe", required=True, help="Path to built sbs_dsw.exe")
    parser.add_argument("--version", required=True, help="Version string (e.g. 1.3.0)")
    parser.add_argument("--notes", default="", help="Optional release notes")
    parser.add_argument("--url", default="sbs_dsw.exe", help="Manifest 'url' value (default: sbs_dsw.exe)")
    parser.add_argument("--exe-name", default="sbs_dsw.exe", help="Output exe filename (default: sbs_dsw.exe)")
    parser.add_argument("--manifest-name", default="manifest.json", help="Manifest filename (default: manifest.json)")
    parser.add_argument(
        "--out-dir",
        default=str(Path(__file__).resolve().parent / "public"),
        help="Output directory (default: tools/update_server/public)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    src_exe = Path(args.exe).resolve()
    if not src_exe.exists():
        raise SystemExit(f"EXE not found: {src_exe}")

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    dst_exe = out_dir / args.exe_name
    shutil.copy2(src_exe, dst_exe)

    digest = sha256_file(dst_exe)
    manifest = {
        "version": str(args.version).strip(),
        "url": str(args.url).strip(),
        "sha256": digest,
    }
    notes = str(args.notes).strip()
    if notes:
        manifest["notes"] = notes

    manifest_path = out_dir / args.manifest_name
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    print(f"Published EXE:      {dst_exe}")
    print(f"SHA256:             {digest}")
    print(f"Published manifest: {manifest_path}")
    print("Manifest payload:")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
