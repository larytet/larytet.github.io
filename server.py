import ssl
import http.server

# HTTPRequestHandler class
class RequestHandler(http.server.BaseHTTPRequestHandler):
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type','text/html')
	self.send_header("Access-Control-Allow-Origin", "*")
	self.send_header("Access-Control-Allow-Methods", "*")
	self.send_header("Access-Control-Allow-Headers", "*")
	self.send_header("Access-Control-Max-Age", "1")
        self.end_headers()
        # Send message back to client
        message = open("index.html", "r").read()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

port=443
print("Using port", port)
httpd = http.server.HTTPServer(('0.0.0.0', port), RequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True, certfile='cert.pem')
httpd.serve_forever()

