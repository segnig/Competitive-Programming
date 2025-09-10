# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        res = 0
        for right in range(len(s)):
            if s[right] == "0":
                res += right - l
                l += 1
        return res   