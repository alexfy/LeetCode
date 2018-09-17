# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:34:52 2018

@author: hwny-in-fuy
"""

class Solution:
    def toLowerCase(self, x):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for i in x:
            res += i.lower()
        return res