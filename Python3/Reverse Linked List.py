# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:54:40 2018

@author: hwny-fuy
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class My_Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        vals = []
        cur = head
        while cur!=None:
            vals.append(cur.val)
            cur = cur.next
        N = len(vals)
        res = ListNode(vals[-1])
        cur = res
        for i in reversed(range(0,N-1)):
            cur.next = ListNode(vals[i])
            cur = cur.next
        return res
    
class Iterative_Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        pre = None
        nex = None
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

class Recursive_Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)
    
    def reverse(self, cur, pre = None):
        if not cur:
            return pre
        nex = cur.next
        cur.next = pre
        return self.reverse(nex,cur)