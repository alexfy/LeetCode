# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:20:19 2018

@author: hwny-in-fuy
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res