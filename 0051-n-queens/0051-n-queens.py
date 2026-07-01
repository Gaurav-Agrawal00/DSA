# class Solution:

    # def isSafe(self,board,row,col,n):
    #     nrow = row
    #     ncol = col - 1
    #     while ncol >= 0:
    #         if board[nrow][ncol] == 'Q':
    #             return False
    #         ncol -= 1
        
    #     nrow = row-1
    #     ncol = col -1
    #     while(nrow >= 0 and ncol >= 0):
    #         if board[nrow][ncol] == 'Q':
    #             return False
    #         ncol -= 1
    #         nrow -= 1

    #     nrow = row + 1
    #     ncol = col -1
    #     while(nrow < n and ncol >= 0):
    #         if board[nrow][ncol] == 'Q':
    #             return False
    #         ncol -= 1
    #         nrow += 1
    #     return True

    # def findNQueens(self,col,board,ans,n):
    #     if col == n:
    #         temp = [''.join(row) for row in board]
    #         ans.append(temp)
    #         return
        
    #     for row in range(n):
    #         if self.isSafe(board,row,col,n) :
    #             board[row][col] = 'Q'
    #             self.findNQueens(col+1,board,ans,n)
    #             board[row][col] = '.'
                
    # def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [['.' for i in range(n)]for j in range(n)]
        # ans = []
        # self.findNQueens(0,board,ans,n)
        # return ans

class Solution:

    def findNQueens(self,col,board,n,ans,leftRow,upperDiagonal,lowerDiagonal):
        if col == n:
            temp = [''.join(row) for row in board]
            ans.append(temp)
            return
        
        for row in range(n):
            if leftRow[row] == False and lowerDiagonal[row+col] == False and upperDiagonal[n-1+col-row] == False:
                leftRow[row] = True
                lowerDiagonal[row+col] = True
                upperDiagonal[n-1+col-row] = True

                board[row][col] = 'Q'
                self.findNQueens(col+1,board,n,ans,leftRow,upperDiagonal,lowerDiagonal)
                leftRow[row] = False
                lowerDiagonal[row+col] =False
                upperDiagonal[n-1+col-row] = False
                board[row][col] = '.'


    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for i in range(n)]
        leftRow  = [False]*n
        upperDiagonal = [False]*(2*n-1)
        lowerDiagonal = [False]*(2*n-1)
        ans = []
        self.findNQueens(0,board,n,ans,leftRow,upperDiagonal,lowerDiagonal)
        return ans