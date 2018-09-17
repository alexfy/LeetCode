# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:57:56 2018

@author: hwny-in-fuy
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1;
        for coin in coins:
            for i in xrange(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]