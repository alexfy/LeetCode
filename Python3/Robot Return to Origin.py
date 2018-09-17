# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:37:40 2018

@author: hwny-in-fuy
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if (len(moves)%2==1):
            return False
        h,v=0,0
        for m in moves:
            if m == 'U':
                v+=1
            elif m =='D':
                v-=1
            if m == 'L':
                h+=1
            elif m =='R':
                h-=1
        return h == 0 and v == 0