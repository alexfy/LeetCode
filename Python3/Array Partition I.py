# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:36:30 2018

@author: hwny-fuy
"""

class My_Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[0:-1:2])

class One_Line_Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])