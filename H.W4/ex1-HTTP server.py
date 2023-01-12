from http.server import  CGIHTTPRequestHandler, HTTPServer
handler = CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]
server = HTTPServer(("localhost", 8080), handler)
server.serve_forever()