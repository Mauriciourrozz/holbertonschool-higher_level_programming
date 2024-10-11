import http.server
import json

PORT = 8000

class My_Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            dic = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dic).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write('OK'.encode('utf-8'))

        elif self.path == '/info':
            dicc = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(json.dumps(dicc).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("404 - Página no encontrada")

with http.server.HTTPServer(("", PORT), My_Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
