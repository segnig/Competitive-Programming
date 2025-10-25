# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # original nums
        original = x
        result = 0

        while x > 0:
            res = x % 10
            x //= 10
            result = result * 10 + res
        
        return result == original
        