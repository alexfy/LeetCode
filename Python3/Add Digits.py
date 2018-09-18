# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:20:57 2018

@author: hwny-in-fuy
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1+(num-1)%9 if num!=0 else 0