'''
Need to use stack to keep track of closing brackets
and dictionary to match closing brackets with corresponding starting ones
'''
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
                    ")":"(",
                    "}":"{",
                    "]":"["
                   }
        stack = []
        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            elif s[i] in brackets.keys():
                if not stack or stack.pop() != brackets[s[i]]:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True