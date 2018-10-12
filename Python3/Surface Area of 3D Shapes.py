# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:02:08 2018

@author: hwny-fuy
"""

class Simple_Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]: res += 2 + grid[i][j] * 4
                if i: res -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
        return res
    
class One_Line_Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(v * 4 + 2 for row in grid for v in row if v) - sum(min(a, b) * 2 for row in grid + list(zip(*grid)) for a, b in zip(row, row[1:]))