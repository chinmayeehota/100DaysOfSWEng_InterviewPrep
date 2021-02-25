'''
Brute Force

Approach:
	Find all possible start and end indexes and check 
	for each combination if it is a palindrome, return the longest palindrome

Time - 0(n^3)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        res = s[0]
        for i in range(len(s)):
            while i < end:
                if self.isPalindrome(s[i:end]) and len(s[i:end]) > len(res):
                    res = s[i:end]
                end -= 1
            end = len(s)
        return res
                
    def isPalindrome(self, string):
        start, end = 0, len(string) -1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True