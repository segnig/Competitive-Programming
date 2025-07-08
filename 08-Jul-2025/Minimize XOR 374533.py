# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bit = num1.bit_count()
        num2_bit = num2.bit_count()
        
        if num1_bit == num2_bit:
            return num1
        
        result = 0
        if num1_bit > num2_bit:
            for i in reversed(range(32)):
                if num1 & (1 << i):
                    result |= (1 << i)
                    num2_bit -= 1
                if num2_bit == 0:
                    break
        else:
            result = num1
            for i in range(32):
                if (result & (1 << i)) == 0:
                    result |= (1 << i)
                    num1_bit += 1
                if num1_bit == num2_bit:
                    break

        return result