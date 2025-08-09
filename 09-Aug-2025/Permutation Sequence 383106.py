# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        re = [k for k in range(1, n+1)]
        pr = list(permutations(re))
        r = ""
        for i in pr[k-1]:
            r += str(i)

        return r
        