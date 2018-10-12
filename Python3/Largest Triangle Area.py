# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:36:41 2018

@author: hwny-fuy
"""

class BF_Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import itertools
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(points, 3))