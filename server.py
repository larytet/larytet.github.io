import SimpleHTTPServer
import ssl


class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")


port=443
print("Using port", port)
httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', port), HandlerClass=MyHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True, certfile='cert.pem')
httpd.serve_forever()

