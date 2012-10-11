import os

for f in os.listdir(os.path.dirname(__file__)):
    file, _ = os.path.splitext(f)
    code = 'from %(module)s import *' % {'module' : file} 
    exec code
