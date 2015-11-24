__author__ = 'Jason'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = [nums[x] for x in range(len(nums)) if nums[x] != nums[x-1] or x == 0]
        return len(nums)