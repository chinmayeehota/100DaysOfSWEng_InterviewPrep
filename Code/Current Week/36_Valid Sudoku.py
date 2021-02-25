'''
Approach 
- for each cell in board check if 
    - valid Row
    - valid Col
    - val 3*3 grid
- Time : O(1)
- Space : O(1)
(Since input size is constant)
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    self.curr_ele = board[row][col]
                    if not self.validRow(row, col) or not self.validCol(row, col) or not self.validGrid(row, col):
                        return False
        return True
    
    def validRow(self, row, col):
        for row_check in range(len(self.board)):
            if row_check != row and self.board[row_check][col] == self.curr_ele:
                print("1")
                return False
        return True
            
    def validCol(self, row, col):
        for col_check in range(len(self.board[0])):
            if col_check != col and self.board[row][col_check] == self.curr_ele:
                print("2")
                return False
        return True
    
    def validGrid(self, row, col):
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        
        for rowIdx in range(3):
            for colIdx in range(3):
                row_check = startRow + rowIdx
                col_check = startCol + colIdx
                if row != row_check and col != col_check and self.curr_ele == self.board[row_check][col_check]:
                    return False
        return True