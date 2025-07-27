# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        memo = {}
        
        def helper(r, k):
            if k == len(key):
                return 0
            if (r, k) in memo:
                return memo[(r, k)]
            
            result = inf
            for i, char in enumerate(ring):
                if key[k] == char:
                    min_dist = min(abs(i - r), len(ring) - abs(i - r)) + 1
                    result = min(result, min_dist + helper(i, k + 1))
            memo[(r, k)] = result
            return result
        return helper(0, 0)
        