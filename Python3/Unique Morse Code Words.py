# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:37:47 2018

@author: hwny-in-fuy
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        map_=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res=set()
        
        for word in words:
            val=""
            for s in word:
                val+=map_[ord(s)-ord('a')]
            res.add(val)
        
        return len(res)