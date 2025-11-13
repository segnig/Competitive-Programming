# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            result += min(n - i, limit) - max(0, n - i - limit) + 1
        return result