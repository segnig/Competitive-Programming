# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c) + 1)

        while left <= right:
            hyp = left * left + right * right

            if hyp == c:
                return True
            elif hyp < c:
                left += 1
            else:
                right -= 1
        
        return False