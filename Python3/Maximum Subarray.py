# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:23:49 2018

@author: hwny-fuy
"""

#Kadane Algorithm
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0: return None
        max_so_far = max_ending_here = nums[0]
        for i in range(1,N):
            max_ending_here = max(nums[i],nums[i]+max_ending_here)
            max_so_far = max(max_so_far,max_ending_here)
        return max_so_far