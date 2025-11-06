# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        counter = defaultdict(int)
    
        left = 0
        answer = 0
        
        for right in range(len(word)):
            while counter[word[right]] > 0:
                counter[word[left]] -= 1
                left += 1
            counter[word[right]] += 1
            answer = max(answer, right - left + 1)
        
        return answer