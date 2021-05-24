# Create an HTTPS server in Python 


Requirement Python 3
Module http.server

First create a key and cert for the server then use SimpleHTTPRequestHandler to create a very basic and simple directory base HTTPS Web Server.

# Python code to start a HTTPS server
```
import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 8443), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='localhost.key',
                               certfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
```

# Create SSL and certificate

```
openssl req -new -x509 -keyout localhost.key -out localhost.pem -days 365 -nodes
```



Ref: https://piware.de/2011/01/creating-an-https-server-in-python/
