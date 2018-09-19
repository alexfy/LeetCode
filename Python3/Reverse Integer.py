# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:13:48 2018

@author: hwny-in-fuy
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = ""
        if x<0:
            res+="-"
            x = -x
        while x>0:
            res += str(x%10)
            x //= 10
        try:
            rev = int(res)
        except ValueError:
            rev = 0
        if rev >= 2147483648 or rev < -2147483648:
            rev = 0
        return rev