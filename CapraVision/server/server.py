#! /usr/bin/env python

#    Copyright (C) 2012  Club Capra - capra.etsmtl.ca
#
#    This file is part of CapraVision.
#    
#    CapraVision is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
""" 
"""

import SocketServer
import socket
import sys
import time
import traceback

from threading import Thread
from CapraVision import filterchain

class HandlerContainer (object):
    instance = None       # Singleton
    def __new__(theClass): 
        "methode de construction standard en Python"
        if theClass.instance is None:
            theClass.handlers = []
            theClass.instance = object.__new__(theClass)
        return theClass.instance
    
    def addHandler(self, handler):
        self.handlers.append(handler)        

class VisionClientHandler(SocketServer.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        HandlerContainer().addHandler(self)
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
        # TODO add a try catch and return stack trace to socket
        # http://docs.python.org/library/traceback.html
        while 1:
            try:
                self.data = self.request.recv(1024)
                #print "Received: " + self.data    
                # just send back the same data, but upper-cased
                # self.request.sendall(self.data.upper())
            except:
                traceback.print_exc(file=sys.stdout)
                message = "Invalid command"

class ReusableTCPServer(SocketServer.TCPServer):
    allow_reuse_address = True


class ThreadedTCPServer(SocketServer.ThreadingMixIn, ReusableTCPServer):
        pass
    
class Server:
    def start(self, PORT):
        self.server = ThreadedTCPServer( ("", PORT), VisionClientHandler)
        print "starting server on port " + str(PORT) + "..."
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.server.shutdown() 
            print "server stopped"
            
    def stop(self):
        self.server.shutdown()
        
    def send(self, data):
        handlerContainer = HandlerContainer()
        print "Sending: " + data
        for handler in handlerContainer.handlers:
            #manage disconnection here
            handler.request.send(data)

if __name__ == '__main__':
    PORT=5030
    print "Loading filterchain manager"
    fcmanager = filterchain.FilterchainManager()
    
    server = Server()
    t = Thread(target=server.start, args=(PORT,))
    t.start()
