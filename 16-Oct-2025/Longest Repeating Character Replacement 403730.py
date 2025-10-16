# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        result = left = most_freq = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            most_freq = max(counter[s[right]], most_freq)

            while right - left - most_freq + 1> k:
                counter[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return max(result, len(s) - left)

            