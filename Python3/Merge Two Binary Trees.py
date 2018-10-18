# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:36:43 2018

@author: hwny-fuy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Fast_Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (t1 and t2):
            t3 = TreeNode(t1.val+t2.val)
            t3.left = self.mergeTrees(t1.left,t2.left)
            t3.right = self.mergeTrees(t1.right,t2.right)
            return t3
        else:
            return t1 or t2
        
class My_Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (not t1 and not t2): return None
        elif (not t2): return t1
        elif (not t1): return t2
        t3 = TreeNode(t1.val+t2.val)
        t3.left = self.mergeTrees(t1.left,t2.left)
        t3.right = self.mergeTrees(t1.right,t2.right)
        return t3