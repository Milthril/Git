import sys
import locale
import http.server
import socketserver

addr = len(sys.argv) < 2 and "localhost" or sys.argv[1]
port = len(sys.argv) < 3 and 80 or locale.atoi(sys.argv[2])

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((addr, port), handler)
print ("HTTP server is at: http://%s:%d/" % (addr, port))
httpd.serve_forever()