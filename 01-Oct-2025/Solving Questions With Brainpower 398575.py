# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            
            take = questions[i][0] + dp(i + questions[i][1]+1)
            not_take = dp(i + 1)

            return max(take, not_take)
        
        return dp(0)