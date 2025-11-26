# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for index, cite in enumerate(citations):
            if cite >= index + 1:
                h = index + 1

            else: return h  
        return h