# Problem: Split Two Strings to Make Palindrome - https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        check_palindrome = lambda word: word == word[::-1]

        index = 0
        while index < len(a) - index and a[index] == b[~index]: index += 1
        if check_palindrome(a[:index] + b[index:]) or check_palindrome(a[:-index] + b[-index:]): 
            return True

        index = 0
        while index < len(a) - index and b[index] == a[~index]: index += 1
        if check_palindrome(b[:index] + a[index:]) or check_palindrome(b[:-index] + a[-index:]): 
            return True

        return False