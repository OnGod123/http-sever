from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/collections':
            self._send_html_response('html/collections.html')
        elif self.path == '/views':
            self._send_html_response('html/views.html')
        elif self.path == '/products':
            self._send_html_response('html/products.html')
        else:
            self._send_error_response(404, 'Not Found')

    def _send_html_response(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self._send_error_response(404, 'File Not Found')

    def _send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
