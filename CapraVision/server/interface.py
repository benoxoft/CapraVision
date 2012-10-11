import filterchain
import filters

from filters.implementation import bgr2gray

class ServerInterface:
    
    def __init__(self):
        print "Loading filterchain manager"
        self.fcmanager = filterchain.FilterchainManager()
        
        
        
    def parseData(self, data):
        print "received data:", data
        
        if data == "newfc":
           cmd = Command(self.fcmanager)
           cmd.execute()
            
        if data == "addfilter":
            #TODO search filter folder for desired filter
            self.fcmanager.getCurrentFc().add_filter(filters.BGR2Grayscale())
            
    
    