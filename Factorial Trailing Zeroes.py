__author__ = 'Jason'
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0
        else:
            sums  = 0
            i = 1
            while n//(5*i) >=1:
                sums += n//(5*i)
                i*=5
            return sums
