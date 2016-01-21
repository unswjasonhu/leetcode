class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
         """
        if n <3:
            return 0
        else:
            p = [True] * n
            p[0] = p[1] = False
            for i in xrange(2, int(n ** .5 + 1)):
                if not p[i]:
                    continue
                for j in xrange(i * i, n, i):
                    p[j] = False
            primes = [i for i in xrange(n) if p[i]]
            return len(primes)





