# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:28:30 2018

@author: hwny-in-fuy
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n < 1: return False
        x = math.log(n,3)
        return abs(round(x) - x) < 0.0000000000001