# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:08:58 2018

@author: hwny-in-fuy
"""

"""My solution"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        zeros = deque()
        last=-1
        cur=0
        n=len(nums)
        count = 0
        for cur in range(n):
            if nums[cur]==0:
                zeros.append(cur)
            elif nums[cur]!=0:
                if len(zeros)>0:
                    nums[zeros[0]] = nums[cur]
                    nums[cur] = 0
                    zeros.popleft()
                    zeros.append(cur)

"""Fast solution"""
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        
        insertIndex = 0
        for n in nums:
            if n != 0:
                nums[insertIndex] = n
                insertIndex += 1
        
        for i in range(insertIndex, len(nums)):
            nums[i] = 0

"""Short solution"""         
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = [x for x in nums if x != 0] + [x for x in nums if x == 0]