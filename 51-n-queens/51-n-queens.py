class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for i in range(n)] for j in range(n)]
        return (self.nqueens(board, 0, []))
        
    def nqueens(self, board, row, ans) -> list[list[str]]:
        if row == len(board):
            a = []
            for r in board:
                s = ''
                for each in r:
                    if each == 1:
                        s += "Q"
                    else:
                        s += "."
                a.append(s)
            ans.append(a)
            return ans
        for col in range(len(board)):
            if self.isValid(board, row, col):
                board[row][col] = 1
                self.nqueens(board, row + 1, ans)
                board[row][col] = 0
        return ans
        
    def isValid(self, board, row, col):
        for i in range(0, row):
            if board[i][col] == 1:
                return False
        maxLeft = min(col, row)
        for i in range(maxLeft+1):
            if board[row-i][col-i] == 1:
                return False
        maxRight = min(row, len(board) - col - 1)
        for i in range(maxRight+1):
            if board[row-i][col+i] == 1:
                return False
        return True