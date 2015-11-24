__author__ = 'Jason'
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if type(num) == int:
            if num >= 10:
                while num >=10:
                    sum = 0
                    for i in list(str(num)):
                        sum += int(i)
                    num = sum
                return num

            elif num >=0 and num < 10:
                return num
            else:
                return False
        else:
            print "please enter a number"