# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def help(word):
            index = 0
            for char in word:
                if (index >= len(pattern) or char != pattern[index]) and "A" <= char <= "Z":
                    return False

                if index < len(pattern) and char == pattern[index]:
                    index += 1
            
            return index >= len(pattern)
        
        result = []

        for word in queries:
            result.append(help(word))
        
        return result