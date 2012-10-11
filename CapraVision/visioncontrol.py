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
        self.parseData(data)

    def parseData(self, data):
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