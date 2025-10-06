# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = defaultdict(int)

        for num in arr:
            if counter[k - num%k] > 0:
                counter[k- num%k] -= 1
            else:
                counter[num%k] += 1
    
        for num in counter:
            if counter [num] != 0 and num != 0:
                return False
        return True