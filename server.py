import BaseHTTPServer, SimpleHTTPServer
import ssl
port=443
print("Using port", port);
httpd = BaseHTTPServer.HTTPServer(('localhost', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True, certfile='cert.pem')
httpd.serve_forever()
