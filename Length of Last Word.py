__author__ = 'Jason'

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.split(' ')
        for i in range(len(list1)):
            if len(list1[-i-1]) == 0:
                pass
            else:
                return len(list1[-i-1])
        return 0

