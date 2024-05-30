#!/usr/bin/env python3
"""Module to fetches all post from JSONPlaceholder API."""
import http.server
import socketserver
import json


class HttpServer(http.server.BaseHTTPRequestHandler):
    """Class to handle HTTP requests."""

    def do_GET(self):
        """Handle GET request."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        else:
            self.send_error(404, "Endpoint not found.")


PORT = 8000

with socketserver.TCPServer(("", PORT), HttpServer) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
