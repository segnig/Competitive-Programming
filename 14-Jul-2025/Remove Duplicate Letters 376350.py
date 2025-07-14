# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        counter_word = Counter(s)
        in_stack = 0
        stack = []

        for char in s:
            counter_word[char] -= 1
            bit = 1 << (ord(char) - ord("a"))
            if in_stack & bit:
                continue
            while stack and char < stack[-1] and counter_word[stack[-1]] > 0:
                popped_char = stack.pop()
                in_stack ^= 1 << (ord(popped_char) - ord("a"))
                
            
            stack.append(char)
            in_stack |= bit
        
        return "".join(stack)
