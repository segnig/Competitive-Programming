# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            odd = self.helper(s, i, i)
            if len(odd) > len(result):
                result = odd
            even = self.helper(s, i, i+1)
            if len(even) > len(result):
                result = even
        
        return result


    def helper(self,word, left, right):
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left+1:right]