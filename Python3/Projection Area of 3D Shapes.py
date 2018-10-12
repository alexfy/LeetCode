# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:18:07 2018

@author: hwny-fuy
"""
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return (sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(v > 0 for row in grid for v in row))
        #zip(*grid) is to transpose grid