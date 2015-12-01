__author__ = 'Jason'
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for n in range(9):
                        if board[i][j] == board[i][n] and j !=n:
                            return False
                        else:
                            for n in range(9):
                                if board[i][j] == board[n][j] and i != n:
                                    return False
                                else:
                                    pass
        n = 1
        m = 3
        while n <=3:
            p = 1
            q = 3
            while p <=3:
                a = []
                for i in range(n*m-3,n*m):
                    for j in range(p*q-3,p*q):
                        if board[i][j] != '.':
                            a.append(board[i][j])
                if len(a) != len(set(a)):
                    return False
                else:
                    p+=1
            n+=1
        return True