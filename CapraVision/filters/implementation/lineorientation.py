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

import cv2
import cv2.cv as cv
import math
import numpy as np

class LineOrientation:
    """Port of the old line detection code"""
    
    def __init__(self):

        self.area_min = 300
        self.area_max = 35000
    
        self._kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3), (0,0))
                
    def execute(self, image):
        image_threshold = cv2.split(image)[0]
        image_morphology = cv2.morphologyEx(
                    image_threshold, cv2.MORPH_CLOSE, self._kernel, iterations=1)
                
        contours, hierarchy = cv2.findContours(
                                            image_morphology, 
                                            cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
        lines = self.find_lines(contours, image)
        self.draw_lines(lines, image)
        
        return image
    
    def draw_lines(self, lines, image):
        for l, t in lines:
            vx, vy, x, y = l
            point1 = (x - t * vx, y - t * vy)
            point2 = (x + t * vx, y + t * vy)
            cv2.line(image, point1, point2, (0, 0, 255), 3, -1)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            
    def find_lines(self, contours, image):
        lines = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0, False)
                                      #cv2.arcLength(contour, False), False)
            area = np.abs(cv2.contourArea(contour))
            
            if self.area_min < area < self.area_max:
                line_values = cv2.fitLine(approx, cv.CV_DIST_L2, 0, 0.01, 0.01)
                rect = cv2.boundingRect(approx)
                t = math.sqrt((rect[2]**2 + rect[3]**2) / 2.0)
                lines.append((line_values, t))
                cv2.drawContours(image, contour, -1, (255, 255, 0))

        return lines
    