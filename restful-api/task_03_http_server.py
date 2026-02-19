#!/usr/bin/python3
""" simple http server module """


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIhandler(BaseHTTPRequestHandler):
    """ mini API that send responses"""
    def do_GET(self):
        """ methods that defines responses for given path """
        if self.path == "/":
            body = "Hello; this is a simple API!".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/status":
            body = "OK".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        else:
            body = "Endpoint not found".encode("utf-8")
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
