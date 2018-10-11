# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:03:41 2018

@author: hwny-fuy
"""

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        if N<3: return 0
        res = 0
        ari_diff = A[1]-A[0]
        ari_len = 2
        for i in range(2,N):
            cur_diff = A[i]-A[i-1]
            if cur_diff == ari_diff:
                ari_len += 1
            else:
                if ari_len != 2:
                    res += (ari_len - 1) * (ari_len - 2) // 2
                    ari_len = 2
                ari_diff = cur_diff
        res += (ari_len - 1) * (ari_len - 2) // 2
        return res