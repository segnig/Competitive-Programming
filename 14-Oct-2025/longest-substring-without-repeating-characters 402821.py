# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)

        left = 0
        result = 0

        for right in range(len(s)):
            while window[s[right]] > 0:
                window[s[left]] -= 1
                left += 1
            window[s[right]] += 1
            result = max(result, right - left + 1)
        
        return result