# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        for char in s_counter:
            if s_counter[char] != t_counter[char]:
                return False
        return True