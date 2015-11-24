__author__ = 'Jason'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            j = 0
            if nums[i] == 0:
                nums.append(0)
                j +=1
            for item in range(j):
                nums.remove(0)
        print nums
