__author__ = 'Jason'
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers= [nums[i] for i in range(len(nums))]
        numbers.sort(reverse=True)
        if numbers[-1]>=0:
            targets = [numbers[i] for i in range(len(numbers)) if numbers[i] <= target]
            for j in range(len(targets)):
                k = target - targets[j]
                num = [targets[i] for i in range(len(targets))]
                num.sort()
                for m in range(len(num)):
                    if m != (len(targets)- j+1):
                        if num[m] == k:
                            q = 0
                            for n in range(len(nums)):
                                if nums[n] == k and q == 0:
                                    second = n + 1
                                    q +=1
                                elif nums[n] == target - k:
                                    first = n + 1
                            if first < second:
                                return first, second
                            else:
                                return second, first
                        if num[m] > k:
                            break
        else:
            for j in range(len(numbers)):
                k = target - numbers[j]
                num = [numbers[i] for i in range(len(numbers))]
                num.sort()
                for m in range(len(num)):
                    if m != (len(numbers)- j+1):
                        if num[m] == k:
                            q = 0
                            for n in range(len(nums)):
                                if nums[n] == k and q == 0:
                                    second = n + 1
                                    q +=1
                                elif nums[n] == target - k:
                                    first = n + 1
                            if first < second:
                                return first, second
                            else:
                                return second, first
                        if num[m] > k:
                            break