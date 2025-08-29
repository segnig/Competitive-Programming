# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = sorted(candidates)
        self.target = target
        self.backtrack(0)
        return self.res

    def backtrack(self, index = 0, total_sum = 0, comb=[]):
        if total_sum == self.target:
            self.res.append(comb[::])
            return 
        if total_sum > self.target or index >= len(self.candidates):
            return 
        
        
        comb.append(self.candidates[index])
        total_sum += self.candidates[index]
        self.backtrack(index, total_sum, comb)
        comb.pop()
        total_sum -= self.candidates[index]
        self.backtrack(index + 1, total_sum, comb)