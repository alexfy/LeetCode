# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:26:48 2018

@author: hwny-fuy
"""

class My_Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        B = bin(N)
        S = len(B)
        res = 0
        prev = -1
        for i in range(S):
            if(B[i]=='1'):
                if(prev>0):
                    res = max(res,i-prev)
                prev = i
        return res