#from http.server import HTTPServer, BaseHTTPRequestHandler 
import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 8443), http.server.SimpleHTTPRequestHandler)
#httpd = HTTPServer(('localhost', 8443), BaseHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='localhost.key',
                               certfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()
