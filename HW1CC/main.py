from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'Hello, world!'}
        self.wfile.write(json.dumps(response).encode())


server_address = ('', 8081)
httpd = HTTPServer(server_address, APIHandler)

print('Starting server...')
httpd.serve_forever()
