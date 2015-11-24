__author__ = 'Jason'
class Solution(object):
    def searchcol(self,matrix,row,target):
        lowcol = 0
        highcol = len(matrix[0]) -1
        while lowcol <= highcol:
            midcol = (lowcol + highcol) /2
            if matrix[row][midcol] > target:
                highcol= midcol -1
            elif matrix[row][midcol] < target:
                lowcol = midcol +1
            else:
                return True
        return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lowrow = 0
        highrow = len(matrix) - 1
        while lowrow <= highrow:
            midrow = (highrow+lowrow) //2
            if matrix[midrow][0] > target:
                if midrow ==lowrow:
                    return False
                else:
                    if matrix[midrow - 1][0] > target:
                        highrow = midrow - 2
                    else:
                        return self.searchcol(matrix,midrow-1,target)
            elif matrix[midrow][0] < target:
                if midrow == highrow:
                   return self.searchcol(matrix,midrow,target)
                else:
                    if matrix[midrow + 1][0] < target:
                        lowrow = midrow +1
                    elif matrix[midrow + 1][0] > target:
                       return self.searchcol(matrix,midrow,target)
                    else:
                        return self.searchcol(matrix,midrow+1,target)
            else:
                return self.searchcol(matrix,midrow,target)
        return False
