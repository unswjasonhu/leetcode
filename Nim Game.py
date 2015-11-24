__author__ = 'Jason'
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if type(n) == int:
            if n % 4 != 0:
                return  True
            else:
                return False
        else:
            print "please enter a number."