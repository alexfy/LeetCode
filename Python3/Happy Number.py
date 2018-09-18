# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:49:17 2018

@author: hwny-in-fuy
"""

class Solution:
    def cal(self,n):
        s = 0
        while n>0:
            s += (n%10)**2
            n = n//10
        return s
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n
        y = n
        count = 0
        while n>1:
            x = self.cal(x)
            if (x==1): return True
            y = self.cal(self.cal(y))
            if (y==1): return True
            if(x==y): return False
        return True