# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        intervals.sort()

        result = []
        for start, end in intervals:
            if result and result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result