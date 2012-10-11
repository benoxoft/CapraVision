from CapraVision import filterchain

class NewFilterchainCommand:
    
    def execute(self, inputControl, FcControl, commandContent):
        FcControl.setCurrentFilterchain(filterchain.FilterChain())
        print "NewFilterchainCommand: New filterchain created."