__author__ = 'Jason'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            key = str(num)
            if key not in d:
                d[key] = 1
            else:
                d[key] +=1
        c = sorted(d.iteritems(), key=lambda d:d[1],reverse = True)
        return int(c[0][0])