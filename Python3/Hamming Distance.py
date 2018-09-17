# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:00:33 2018

@author: hwny-in-fuy
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x^y
        return bin(tmp).count("1")