# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:37:40 2018

@author: hwny-fuy
"""
import math

class Formula_Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((((math.sqrt(5)+1)/2)**(n+1)-((1-math.sqrt(5))/2)**(n+1))/math.sqrt(5))

class Iterative_Solution:
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return 1
        res = 0 #F[n]
        one = 1 #F[n-1]
        two = 1 #F[n-2]
        for i in range(2,n+1):
            res = one + two
            two = one
            one = res
        return res

class Memoization_Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return 1
        F = [1]*(n+1)
        for i in range(2,n+1):
            F[i] = F[i-1]+F[i-2]
        return F[n]