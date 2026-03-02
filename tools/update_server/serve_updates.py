import argparse
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


class UpdateRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/healthz":
            payload = b"ok\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()

    def end_headers(self):
        # Avoid stale manifest caching on clients.
        if self.path.endswith("/manifest.json") or self.path == "/manifest.json":
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
        super().end_headers()


def parse_args():
    parser = argparse.ArgumentParser(description="Serve SBS DSW update files (manifest + exe) over HTTP.")
    parser.add_argument("--host", default="0.0.0.0", help="Bind address (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8080, help="Bind port (default: 8080)")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent / "public"),
        help="Directory to serve (default: tools/update_server/public)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    os.chdir(root)

    server = ThreadingHTTPServer((args.host, args.port), lambda *a, **k: UpdateRequestHandler(*a, directory=str(root), **k))
    print(f"Serving update files from: {root}")
    print(f"Manifest URL: http://{args.host}:{args.port}/manifest.json")
    print(f"Health URL:   http://{args.host}:{args.port}/healthz")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
