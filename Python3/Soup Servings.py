# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:55:33 2018

@author: hwny-fuy
"""

import math

class Solution:
    memo = {}
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800: return 1.0
        
        def f(A,B):
            if (A,B) in self.memo: return self.memo[(A,B)]
            elif (A <= 0 and B <= 0): return 0.5
            elif (A <= 0): return 1
            elif (B <= 0): return 0
            self.memo[(A,B)] = 0.25 * (f(A-4,B)+f(A-3,B-1)+f(A-2,B-2)+f(A-1,B-3))
            return self.memo[(A,B)]
        
        N = math.ceil(N/25.0)
        return f(N,N)