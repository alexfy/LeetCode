# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:35:47 2018

@author: hwny-fuy
"""

class My_Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = -1000, -1000, -1000
        min1, min2= 1000, 1000
        for n in nums:
            tmp = n
            if(tmp>max1):
                tmp,max1 = max1,tmp
            if(tmp>max2):
                tmp,max2 = max2,tmp
            if(tmp>max3):
                tmp,max3 = max3,tmp
            tmp = n
            if(tmp<min1):
                tmp,min1 = min1,tmp
            if(tmp<min2):
                tmp,min2 = min2,tmp
        return max(max1*max2*max3,max1*min1*min2)

class Slightly_Faster_Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = -1000, -1000, -1000
        min1, min2= 1000, 1000
        for n in nums:
            if(n>max1):
                max3 = max2
                max2 = max1
                max1 = n
            elif(n>max2):
                max3 = max2
                max2 = n
            elif(n>max3):
                max3 = n
            if(n<min1):
                min2 = min1
                min1 = n
            elif(n<min2):
                min2 = n
        return max(max1*max2*max3,max1*min1*min2)