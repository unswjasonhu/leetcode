__author__ = 'Jason'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=[]
        if n <= 2:
            return n
        else:
            x.append(1)
            x.append(2)
            for i in range(n-2):
                x.append((x[i]+x[i+1]))
            return x[-1]