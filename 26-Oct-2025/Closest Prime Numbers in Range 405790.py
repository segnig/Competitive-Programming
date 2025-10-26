# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        is_prime = [1] * (right + 1)
        is_prime[0], is_prime[1] = 0, 0

        for i in range(2, int(right** 0.5 )+1):
            if is_prime[i]:
                for j in range(i*i, right + 1, i):
                    is_prime[j] = 0

        primes = []

        for num in range(left, right + 1):
            if is_prime[num] == 1:
                primes.append(num)

        result = None

        for i in range(1, len(primes)):
            if not result:
                result = [primes[i-1], primes[i]]

            elif primes[i] - primes[i-1] < result[1] - result[0]:
                result = [primes[i-1], primes[i]]

        return result if result else [-1, -1]                