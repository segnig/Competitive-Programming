# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution(object):
    def distinctPrimeFactors(self, ns):
        def fact(n):
            store = set()
            dv = 2
            while n != 1:
                if n % dv == 0:
                    store.add(dv)
                    while n % dv == 0:
                        n /= dv
                dv += 1
            return store

        store = []

        for n in range(2, 1001):
            store.append(fact(n))

        result = set()
        for n in ns:
            result |= store[n-2]

        return len(result)
        