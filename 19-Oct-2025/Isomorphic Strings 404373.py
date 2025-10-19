# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace_s = {}
        replace_t = {}


        for i in range(len(s)):
            if s[i] not in replace_s:
                replace_s[s[i]] = t[i]
            if t[i] not in replace_t:
                replace_t[t[i]] = s[i]
            
            if t[i] != replace_s[s[i]] or s[i] != replace_t[t[i]]:
                return False
        
        return True