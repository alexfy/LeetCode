# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:23:49 2018

@author: hwny-in-fuy
"""

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        cur = self.robHelper(root)
        return max(cur[0],cur[1])
    
    def robHelper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return [0,0]
        if(root.left==None and root.right == None):
            return [root.val,0]
        left = self.robHelper(root.left)
        right = self.robHelper(root.right)
        s = root.val + left[1] + right[1]
        t = max(left[0],left[1]) + max(right[0],right[1])
        return [s,t]