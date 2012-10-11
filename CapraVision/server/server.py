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

import socket

from threading import Thread

class Server:
    
    def __init__(self):
        self.handlers = []
    
    def start(self, ip, port):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((ip, port))
        print "Server awaiting connections on port " + str(port)
        
        self.done = False
        while not self.done:
            s.listen(1)
            conn, addr = s.accept()
            print 'Connected to:', addr
            handler = ClientHandler(conn, self.visionControlCallback)
            self.handlers.append(handler)
            t = Thread(target=handler.handle)
            t.start()           

            
    def stop(self):
        self.done = True
        
    def send(self, data):
        for handler in self.handlers:
            handler.send(data)
            
    def register(self, callback):
        self.visionControlCallback = callback
        
    def notifyCallback(self, data):
        self.visionControlCallback(data)
    
class ClientHandler:
    
    def __init__(self, conn, callback):
        self.done = False
        self.conn = conn
        self.callback = callback
    
    def handle(self):
        while not self.done:
            data = self.conn.recv(1024)
            if not data: 
                break
            self.callback(data)
            #self.conn.send(data)  # echo
            #self.conn.close()
            
    def stop(self):
        self.done = True
        
    def send(self, data):
        self.conn.send(data)
    
    
