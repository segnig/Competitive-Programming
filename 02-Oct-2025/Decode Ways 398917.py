# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            single = dp(i+1)
            two = 0

            if i < len(s)-1 and "10" <= s[i:i+2] <= "26":
                two = dp(i+2)
            
            return single + two
        return dp(0)
            
            