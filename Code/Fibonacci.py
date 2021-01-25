'''
Recursive
Time Complexity : O(2^n)
Space Complexity : 
'''
class Solution:
	def fib(n):
		if n <= 0:
			return 0
		elif n == 1:
			return 1
		else:
			return fib(n-1)+fib(n-2)

'''
Memoization or Bottom Up DP
Time Complexity : O()
Space Complexity : O()
'''
class Solution:
    def fib(self, n: int, memo={0:0, 1:1}) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        for i in range(2, n+1):
            if i not in memo:
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

'''
Top Down DP
Time Complexity : O()
Space Complexity : O()
'''
class Solution:
    def fib(self, n: int, memo={0:0, 1:1}) -> int:
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]