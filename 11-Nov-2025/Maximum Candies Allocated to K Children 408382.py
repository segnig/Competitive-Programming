# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)

        def checker(x):
            count = 0
            for candy in candies:
                count += candy // x
            
            return count >= k
        
        while left <= right:
            mid = (right + left) // 2
            
            if checker(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
        