from CapraVision import filterchain

from filterchain import chain

class SaveFilterchainCommand:
    
    def execute(self, inputControl, FcControl, commandContent):
        chain.write(commandContent, FcControl.getCurrentFilterchain())
        print "SaveFilterchainCommand: Filterchain " + commandContent + " saved."