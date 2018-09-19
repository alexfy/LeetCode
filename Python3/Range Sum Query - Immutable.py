# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:11:51 2018

@author: hwny-in-fuy
"""

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = {}
        if(len(nums)>0):
            self.sums[0] = nums[0]
            for i in range(1,len(nums)):
                self.sums[i] = self.sums[i-1]+nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if(len(self.sums)==0 or j>=len(self.sums)): return None
        return self.sums[j] if i==0 else self.sums[j]-self.sums[i-1]