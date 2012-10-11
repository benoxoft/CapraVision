from CapraVision import filterchain

class AddFilterCommand:
    
    def execute(self, inputControl, FcControl, commandContent):
        classes = __import__("filters.implementation")
        filterClass = getattr(classes, commandContent)
        FcControl.getCurrentFilterchain().add_filter(filterClass())
        print "AddFilterCommand: filter " + commandContent + " added to filterchain."
        pass;