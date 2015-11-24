__author__ = 'Jason'
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = bin(n)
        y = list(x)
        j = 0
        print y
        for i in y:
            if i == '1':
                j +=1
        return j
