# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        temp = set(stones)
        hashTable = {stone: i for i, stone in enumerate(stones)}

        @cache
        def dp(k, i):
            if i == len(stones) - 1:
                return True
            
            stone = stones[i]
            for step in [k-1, k, k+1]:

                if (step != 0) and (stone + step in temp) and dp(step, hashTable[stone + step]):
                    return True

            return False

        return dp(1, 1)