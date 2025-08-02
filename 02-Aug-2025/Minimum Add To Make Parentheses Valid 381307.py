# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for par in s:
            if stack and stack[-1] != par and par == ")":
                stack.pop()
            else:
                stack.append(par)
        return len(stack)