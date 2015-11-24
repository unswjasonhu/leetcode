__author__ = 'Jason'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] +=1
            return digits
        else:
            if digits.count(9) == len(digits):
                return [1]+[0]*len(digits)
            else:
                for i in range(len(digits)-1):
                    print i
                    print digits[-1]
                    if digits[-i-2] != 9:
                        digits[-1]=0
                        digits[-i-2] +=1
                        digits[-i-1:-1]=[0]*(i)
                        return digits
                        break