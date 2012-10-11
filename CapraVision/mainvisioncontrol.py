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

import os
import server
from threading import Thread

from CapraVision import filterchain
from CapraVision import input
    
class VisionControl:
    
    PORT=5030
    IP="127.0.0.1"
    
    COMMAND_MODULE="command"
    
    def __init__(self):
        self.inputControl = input.InputControl()
        self.filterchainControl = filterchain.FilterchainControl()
        pass
    
    def launch(self):
        self.server = server.Server()
        self.server.register(self.callback)
        t = Thread(target=self.server.start, args=(self.IP, self.PORT,))
        t.start()
        
    def callback(self, data):
        self.parse_data(data)

    def parse_data(self, data):
        self.runCommand(data, "BGR2Grayscale")
            
    def runCommand(self, commandName, commandContent):
        print "running command: " + commandName
        classes = __import__(self.COMMAND_MODULE)
        commandClass = getattr(classes, commandName)
        commandClass().execute(self.inputControl, self.filterchainControl, commandContent)
    
        
if __name__ == '__main__':
    visionControl = VisionControl()
    visionControl.launch()
    #visionControl.runCommand("NewFilterchainCommand", "testsave")
    
    #visionControl.runCommand("AddFilterCommand", "BGR2Grayscale")
    
    #visionControl.runCommand("SaveFilterchainCommand", "testsave")