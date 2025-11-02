# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        # [[1,3],[2,6],[8,10],[15,18]]
        # [1, 6], [8, 10], [15, 18]]

        # sort intervals

        # move over every interval and check we can merge or not 

        intervals.sort()

        merged_intervals = []

        for start, end in intervals:
            if merged_intervals and merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
            else:
                merged_intervals.append([start, end])
        
        # return the merged_intervals
        return merged_intervals