# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:37:37 2018

@author: hwny-in-fuy
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        size1 = len(J)
        size2 = len(S)
        #i,j = 0,0
        count = 0
        for i in range(0,size2):
            cur = S[i]
            for j in range(0,size1):
                if cur == J[j]:
                    count += 1
                    break
        return count