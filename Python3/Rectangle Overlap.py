# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:43:20 2018

@author: hwny-fuy
"""
rec1 = [0,0,1,1]
rec2 = [1,1,3,3]
x = False
x = rec1[0]<rec2[2] or rec1[2]>rec2[0]
y = False
y = rec1[1]<rec2[3] or rec1[3]>rec2[1]
print (x and y)