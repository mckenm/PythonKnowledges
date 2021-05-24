# Create an HTTPS server in Python 


Requirement Python 3
Module http.server

```
import http.server
import ssl

server_address = ('localhost', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()

```

# Create SSL and certificate

```
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
```



Ref: https://piware.de/2011/01/creating-an-https-server-in-python/
