import filters


class FilterchainManager:
    
    def __init__(self):
        pass
    
    def getCurrentFc(self):
        return self.currentFc
    
    def setCurrentFc(self, filter):
        self.currentFc = filter
    
    def save_chain_as(self):
        pass