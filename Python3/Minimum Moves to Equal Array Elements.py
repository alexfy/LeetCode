# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:18:14 2018

@author: hwny-fuy
"""

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)