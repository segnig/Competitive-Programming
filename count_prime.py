#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = []

        inial = [True] * (n + 1)

        if n == 0:
            inial[0] = False

        elif n >= 1:
            inial[0] = False
            inial[1] = False
        for i in range(2, n + 1):
            if inial[i]:
                prime.append(i)
                for j in range(i ** 2, n + 1, i):
                    inial[j] = False
        if n not in prime:
            return len(prime)
        else:
            return len(prime) - 1

# @lc code=end
