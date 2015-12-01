__author__ = 'Jason'

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            a = []
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] == nums[j] and i != j:
                        a.append(abs(i-j))
                    else:
                        pass
            a.sort()
            if a[0] <=k:
                return True
            else:
                return False