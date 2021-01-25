'''
Approach - Recursive
1). 

Time - 
Space - 
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def traverse(m , n, row, col):
            if row > m:
                return 0
            if col > n:
                return 0
            if row == m -1:
                return 1
            if col == n -1:
                return 1
            return traverse(m, n, row+1, col) + traverse(m, n, row, col+1)
        return traverse(m, n, row=0, col=0)

'''
Approach - Memoization
1). 

Time - 
Space - 
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def traverse(m , n, row, col):
            if row >= m:
                return 0
            if col >= n:
                return 0
            if row == m-1:
                return 1
            if col == n-1:
                return 1
            pathSum = [[-1] * n] * m
            if pathSum[row][col] == -1:
                pathSum[row][col] = traverse(m, n, row+1, col) + traverse(m, n, row, col+1)
            return pathSum[row][col]
        return traverse(m, n, row=0, col=0)

'''
Approach - Top Down Dynamic Programming
1). 

Time - 
Space - 
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
        return mem[-1][-1]
