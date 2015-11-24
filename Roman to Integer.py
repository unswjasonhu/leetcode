__author__ = 'Jason'
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        x ={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        nums = [x[i] for i in s]
        numbers = sum(nums)
        for j in range(len(nums)-1):
            if nums[j] < nums[j+1]:
                numbers -= nums[j] *2
        return numbers