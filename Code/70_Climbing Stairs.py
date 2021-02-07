'''
Approach

'''
'''
Recursive
Time - 
Space -
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        #base case
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

'''
Top Down(Memoization)
Time - 
Space -
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for i in range(n)]
        return self.cache(n, memo)
    
    def cache(self, n, memo):
        #base case
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n-1] == -1:
                memo[n-1] = self.cache(n-1, memo) + self.cache(n-2, memo)
        return memo[n-1]

'''
Bottom Up(DP)
Time - 
Space -
'''
class Solution:
    def climbStairs(self, n: int, mem = {}) -> int:
        if n < 0:
            return 0
        elif n in [0, 1]:
            return 1
        mem[0] = 1
        mem[1] = 1
        for i in range(2, n+1):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[n-1] + mem[n-2]