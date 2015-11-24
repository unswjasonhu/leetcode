__author__ = 'Jason'
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = list(s)
        x.reverse()
        print x
        y = 0
        for i in range(len(x)):
            y += (ord(x[i])-64)*(26**i)
        return y