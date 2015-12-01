__author__ = 'Jason'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {'(':')','{':'}','[':']'}
        ls = []
        for i in s:
            if i in dicts:
                ls.append(i)
            else:
                if not ls or dicts[ls.pop()] != i:
                    return False
        if ls:
            return False
        return True

