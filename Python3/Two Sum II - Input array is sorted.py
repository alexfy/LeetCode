# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:21:13 2018

@author: hwny-in-fuy
"""

"""General Solution"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in buff_dict:
                return [buff_dict[numbers[i]]+1,i+1]
            else:
                buff_dict[target-numbers[i]] = i

"""Fast Solution"""
class Solution1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            elif numbers[head] + numbers[tail] < target:
                head += 1
            elif numbers[head] + numbers[tail] == target:
                return [head+1, tail+1]