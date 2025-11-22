# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1
        pos = -1

        while left <= right:
            mid = (right + left) // 2

            if letters[mid] > target:
                right = mid - 1
                pos = mid
            else:
                left = mid + 1
        
        return letters[pos] if pos != -1 else letters[0]