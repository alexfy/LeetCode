# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:27:13 2018

@author: hwny-fuy
"""

class My_Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for n in range(left,right+1):
            tmp = n
            flag = True
            while(tmp!=0):
                digit = tmp%10
                if (digit==0 or n%digit!=0):
                    flag = False
                    tmp = 0
                tmp = tmp//10
            if (flag):
                res.append(n)
        return res

class Short_Solution():
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        return list(filter(is_self_dividing, range(left, right + 1)))