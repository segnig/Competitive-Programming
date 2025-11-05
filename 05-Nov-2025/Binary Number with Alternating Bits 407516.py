# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        is_odd = n % 2 == 1
        n //= 2

        while n:
            temp  = n % 2 == 1
            if is_odd == temp:
                return False
            is_odd = temp
            n //= 2
        
        return True