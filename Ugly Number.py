__author__ = 'Jason'
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x =[]
        j= 2
        if num == 1:
            return True
        elif num <= 0:
            return False
        else:
            while j<= num:
                if num % j ==0:
                    num /=j
                    x.append(j)
                else:
                    j +=1
                    if j  > 5:
                        return False
            return True