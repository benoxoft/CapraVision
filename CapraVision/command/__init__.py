""" Command implementations
    Rules:
        - Command must be a class
        - Filter must have a execute(InputControl, FilterchainControl) function """
        
import os

for f in os.listdir(os.path.dirname(__file__)):
    file, _ = os.path.splitext(f)
    code = 'from %(module)s import *' % {'module' : file} 
    exec code