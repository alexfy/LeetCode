# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:00:11 2018

@author: hwny-fuy
"""

class My_Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return None
        n = len(A)
        oddeven = []
        evenodd = []
        for i in range(n):
            if i%2 == 0 and A[i]%2 != 0:
                if oddeven:
                    A[i],A[oddeven[-1]] = A[oddeven[-1]],A[i]
                    oddeven.pop()
                else:
                    evenodd.append(i)
            elif i%2 == 1 and A[i]%2 != 1:
                if evenodd:
                    A[i],A[evenodd[-1]] = A[evenodd[-1]],A[i]
                    evenodd.pop()
                else:
                    oddeven.append(i)
        return A
    
class Short_Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = [x for x in A if not x%2], [x for x in A if x%2]
        return [even.pop() if not i%2 else odd.pop() for i in range(len(A))]