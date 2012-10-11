import filters


class FilterchainControl:
    
    def __init__(self):
        self.currentFc = None
        pass
    
    def getCurrentFilterchain(self):
        if self.currentFc is None:
            print "ERROR: FilterchainControl currently has no filterchain."
            return None
        else:
            return self.currentFc
    
    def setCurrentFilterchain(self, filterchain):
        self.currentFc = filterchain
    
    def run(self):
        pass