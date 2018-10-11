# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:05:39 2018

@author: hwny-fuy
"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(A)
        if M == 0: return A
        N = len(A[0])
        for i in range(M):
            A[i][0::] = A[i][::-1]
            for j in range(N):
                A[i][j] = 1 if A[i][j] == 0 else 0
        return A