__author__ = 'Jason'

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        totalarea = (C-A)*(D-B) + (G-E)*(H-F)
        x = max(0,min(G,C)-max(A,E))
        y = max(0,min(D,H)-max(B,F))
        return totalarea - x*y