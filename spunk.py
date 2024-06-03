import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randrange

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(f"spunkcronyms.list", "r") as f:
            spunklist = f.readlines()
        x = randrange(len(spunklist))
        spunk = spunklist[x]
        today = f"Your Spunkcronym of the day is: {spunk}"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(today.encode('utf-8'))
    
def run(server_class=HTTPServer, handler_class=HelloWorldHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
