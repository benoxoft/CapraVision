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

import filters

class FilterchainControl:
    
    def __init__(self):
        self.currentFc = None
        pass
    
    def get_current_filterchain(self):
        if self.currentFc is None:
            print "ERROR: FilterchainControl currently has no filterchain."
            return None
        else:
            return self.currentFc
    
    def set_current_filterchain(self, filterchain):
        self.currentFc = filterchain
