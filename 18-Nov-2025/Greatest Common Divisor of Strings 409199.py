# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        result = ""

        l = min(l1, l2)

        for i in range(l):
            a = l1 // (i+1) 
            b = l2 // (i+1)
            if str1[:i+1] * a == str1 and str1[:i+1] * b == str2:
                result = str1[:i+1]
        
        return result

        