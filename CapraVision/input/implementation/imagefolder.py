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

import CapraVision.input.utils
import cv2

class ImageFolder:
    
    def __init__(self):
        self.folder_name = ''
        self.file_names = []
        self.position = 0
        
    def read_folder(self, folder):
        self.file_names = utils.find_all_images(folder)
        self.folder_name = folder
        self.position = 0
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.position >= len(self.file_names):
            raise StopIteration
        else:
            image = self.load_image(self.position)
            self.position += 1
            return image
    
    def load_image(self, position):
        image = self.file_names[position]
        return cv2.imread(image)
        
    def current_position(self):
        return self.position
    
    def total_images(self):
        return len(self.file_names)
    
