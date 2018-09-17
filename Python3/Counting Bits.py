# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:26:20 2018

@author: hwny-in-fuy
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1,num+1):
            res.append(bin(i).count("1"))
        return res
    
    def countBits1(self, num):
        ones = [0]
        for i in range(1,num+1):
            # bitwise trick from @fengcc 's solution
            ones.append(ones[i&(i-1)]+1)    
            
        return ones