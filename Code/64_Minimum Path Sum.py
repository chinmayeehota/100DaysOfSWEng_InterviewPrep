'''
- choose the min one at any point
- chnage grid value in place updating it with the min as we traverse
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if r==0 and c==0:
                    continue
                if r-1 < 0:
                    grid[r][c] += grid[r][c-1]
                elif c-1 < 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[row-1][col-1]