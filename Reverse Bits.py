__author__ = 'Jason'
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 4294967295 or n < 0:
            return False
        else:
            binnum = bin(n)
            binlist = list(binnum)[2:]
            binlist.reverse()
            if len(binlist) < 32:
                n = 32 - len(binlist)
                str0 = ['0']*n
                binlist += str0
                binlist= "".join(binlist)
                return int(binlist,2)
            else:
                binlist= "".join(binlist)
                return int(binlist,2)


