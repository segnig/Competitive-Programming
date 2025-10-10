# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_heights = sorted(heights)

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                count += 1
        
        return count