# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        nums = [[abs(num - x), x < num] for num in arr]
        heapify(nums)
        result = []
        for _ in range(k):
            diff, neg = heappop(nums)
            if neg:
                result.append(x + diff)   
            else:
                result.append(x - diff)  
            
        result.sort()
        return result  