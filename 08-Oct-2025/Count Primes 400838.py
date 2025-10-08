# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * (n + 3)

        prime[0], prime[1] = False, False

        
        for i in range(2, n+1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False
        
        count = 0
        for i in range(2, n):
            if prime[i]:
                count += 1
        
        return count
        