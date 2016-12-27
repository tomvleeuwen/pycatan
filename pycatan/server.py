from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

# Test responses for Kolonisten van FS
import random
import json
import time

TIMEOUT = 5.0

def get_response(cmds):
   # Most of the time, do nothing.
   start = time.time()
   while True:
       to_send = []
       while len(cmds) > 0:
           to_send.append(cmds.pop(0))
       if len(to_send) > 0 or (time.time() - start) > TIMEOUT:
           return json.dumps(to_send)
       time.sleep(0.01)
    
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def MakeHandlerClass(cmds_arg):
    class CustomHandler(BaseHTTPRequestHandler):
        cmds = cmds_arg
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            message = get_response(self.cmds)
            self.wfile.write(message)
            self.wfile.write('\n')
            return

        def end_headers (self):
            self.send_header('Access-Control-Allow-Origin', '*')
            BaseHTTPRequestHandler.end_headers(self)
            
    return CustomHandler

if __name__ == '__main__':
    Handler = MakeHandlerClass([])
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
