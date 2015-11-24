__author__ = 'Jason'
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = {}
        k = 0
        if nums == []:
            return False
        for i in nums:
            if i in x:
                x[i] +=1
            else:
                x[i] = 1
        for j in x.values():
            if j > 1:
                k +=1
        if k != 0:
            return True
        else:
            return False
