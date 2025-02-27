#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(','}':'{',']':'['}
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if not stack or stack.pop() != brackets[bracket]:
                    return False
        return not stack
