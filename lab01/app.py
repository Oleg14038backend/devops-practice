from http.server import BaseHTTPRequestHandler, HTTPServer 




class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"HELLO FROM DevOps lab01\n")

server = HTTPServer(("127.0.0.1", 8080), Handler)
server.serve_forever()
