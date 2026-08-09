#!/usr/bin/env python3
"""Simple HTTP server with no-cache headers for OR Learning Hub."""
import http.server
import os

PORT = 8000
DIR = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

if __name__ == '__main__':
    with http.server.HTTPServer(('', PORT), NoCacheHandler) as httpd:
        print(f"[OK] OR Learning Hub running at:")
        print(f"   http://localhost:{PORT}/app.html")
        print(f"   http://127.0.0.1:{PORT}/app.html")
        print(f"Press Ctrl+C to stop.")
        httpd.serve_forever()
