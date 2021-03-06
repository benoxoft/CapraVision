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
"""
This module contains the code for the sources.
Sources are objects that returns file_names.  
It can be a a webcam, list of files from the hard drive or anything else.

Sources should implement the iterator protocol:
    http://docs.python.org/library/stdtypes.html#iterator-types
"""

import os

for f in os.listdir(os.path.dirname(__file__)):
    file, _ = os.path.splitext(f)
    code = 'from %(module)s import *' % {'module' : file} 
    exec code
