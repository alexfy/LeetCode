# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:12:26 2018

@author: hwny-in-fuy
"""

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while(num%2==0):
            num /=2
        while(num%3==0):
            num /=3
        while(num%5==0):
            num /=5
        return num==1