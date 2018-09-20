# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:38:54 2018

@author: hwny-in-fuy
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dpw1 = [0] * (n+1)
        dpo1 = [0] * (n)
        dpw1[1] = nums[0]
        dpw1[2] = nums[0]
        dpo1[1] = nums[1]
        for i in range(2,n):
            dpw1[i+1] = max(dpw1[i],dpw1[i-1]+nums[i])
            dpo1[i] = max(dpo1[i-1],dpo1[i-2]+nums[i])
        dpw1[n] = max(dpw1[n-1],dpw1[n-2])
        return max(dpw1[n],dpo1[n-1])