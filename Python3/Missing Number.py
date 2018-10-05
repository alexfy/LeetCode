# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:46:53 2018

@author: hwny-fuy
"""

class My_Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0: return 0
        Nexists = False
        for n in nums: 
            if abs(n)!=N:
                nums[abs(n)] *= -1
            else: Nexists = True
        for i in range(0,N):
            if nums[i]>0:
                return i
            elif nums[i]==0:
                x=i
        if Nexists:
            return x
        else:
            return N

class Sum_Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        res = N*(N+1)/2
        for i in range(0,N):
            res -= nums[i]
        return int(res)

class XOR_Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        res = N
        for i in range(0,N):
            res = res^i^nums[i]
        return res

from functools import reduce
class Reduce_XOR_Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        x = reduce(lambda i, j: i ^ j, nums)
        y = reduce(lambda i, j: i ^ j, range(n + 1))
        return x ^ y