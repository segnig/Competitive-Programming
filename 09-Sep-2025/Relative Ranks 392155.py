# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank = {val: index + 1 for index, val in enumerate(sorted_score)}

        result = []
        for val in score:
            result.append(self.ranker(rank[val]))

        return result

    
    def ranker(self, i):
        if i == 1:
            return "Gold Medal"
        if i == 2:
            return "Silver Medal"
        if i == 3:
            return "Bronze Medal"
        return str(i)