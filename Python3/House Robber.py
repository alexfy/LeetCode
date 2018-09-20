# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:50:36 2018

@author: hwny-in-fuy
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        s = [0] * n
        t = [0] * n
        s[0] = nums[0]
        for i in range(1,n):
            s[i] = nums[i] + t[i-1]
            t[i] = max(s[i-1],t[i-1])
        return max(s[n-1],t[n-1])
        

class Solution1:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[n]