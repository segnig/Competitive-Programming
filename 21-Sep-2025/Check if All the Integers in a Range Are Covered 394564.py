# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        store = set()
        for l, r in ranges:
            for num in range(l, r + 1):
                store.add(num)
        
        for num in range(left, right + 1):
            if num not in store:
                return False
        
        return True