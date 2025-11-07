# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:

        vowels = set(["a", "e", "i", "o", "u"])

        result = 0
        count = 1
        n = len(word)
        for i, char in enumerate(word):
            if char in vowels:
                result += (i + 1) * (n - i)
        
        return result
        