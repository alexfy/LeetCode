# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:29:22 2018

@author: hwny-in-fuy
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        if len(s) % 2 == 1: return False
        dic = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for char in s:
            if char in dic:   
                stack.append(char)
            else:
                if not stack or dic[stack.pop()] != char:
                    return False
        return not stack  