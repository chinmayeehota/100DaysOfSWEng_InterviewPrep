'''
Approach
- Two pointer approach
- Return false as soon as condition is not satisfied
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start].lower() != s[end].lower():
                        return False
                    else:
                        start += 1
                        end -= 1
                else:
                    end -= 1
            else:
                start += 1
        return True