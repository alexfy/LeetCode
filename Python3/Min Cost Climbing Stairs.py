# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:26:06 2018

@author: hwny-fuy
"""

# O(N) Space
class My_Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        F = [0] * (N+1)
        for i in range(2,N+1):
            F[i] = min(F[i-1]+cost[i-1],F[i-2]+cost[i-2])
        return F[-1]

# O(1) Space
class Const_Space_Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        mc1,mc2 = cost[0],cost[1]
        for i in range(2,N):
            mc1,mc2 = mc2,min(mc1,mc2)+cost[i]
        return min(mc1,mc2)