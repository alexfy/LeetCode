# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:24:46 2018

@author: hwny-fuy
"""

class My_Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if(len(ops)==0): return m*n
        res = 1
        for v in map(min, zip(*ops)):
            res*=v
        return res