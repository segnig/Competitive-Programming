# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        
        result = [intervals[0]]
        
    
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
               result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        
        return result
        
        
        
        