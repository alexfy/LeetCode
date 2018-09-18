# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:16:01 2018

@author: hwny-in-fuy
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = str(bin(int(a,2)+int(b,2)))
        return x[2:]