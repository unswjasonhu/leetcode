__author__ = 'Jason'
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maps = {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
        nums = map(int,str(n))
        sum = 0
        if n >=2:
            for i in nums:
                sum += maps[i]
            while sum >= 2:
                if sum == 4 or sum == 16 or sum == 37 or sum == 42or sum == 20or sum == 58or sum == 89or sum == 145:
                    return False
                else:
                    sums = map(int,str(sum))
                    print sums
                    sum = 0
                    for j in sums:
                        sum += maps[j]
            else:
                return True
        elif n ==1:
            return True
        else:
            return False