#!/usr/bin/env python3
"""Simple brainstorm companion server - serves newest HTML file in content/."""
import http.server, os, time, threading

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "content")
PORT = 52341

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def do_GET(self):
        files = sorted(
            [f for f in os.listdir(CONTENT_DIR) if f.endswith(".html")],
            key=lambda f: os.path.getmtime(os.path.join(CONTENT_DIR, f))
        )
        if not files:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<p>Waiting for content...</p>")
            return
        path = os.path.join(CONTENT_DIR, files[-1])
        with open(path, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Refresh", "3")
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    with http.server.HTTPServer(("127.0.0.1", PORT), Handler) as srv:
        print(f"Brainstorm server running at http://localhost:{PORT}", flush=True)
        srv.serve_forever()
