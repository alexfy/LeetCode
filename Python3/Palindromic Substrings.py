# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:12:18 2018

@author: hwny-fuy
"""

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        res = 0
        for center in range(2*N-1):
            left = center//2
            right = left+center%2
            while left>=0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res