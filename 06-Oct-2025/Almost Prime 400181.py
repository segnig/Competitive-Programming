# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def prime_factorization(n):
    d = 2

    factorization = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.add(d)
            n //= d
        d += 1
    if n > 1:
        factorization.add(n)

    return factorization

num = int(input())

count = 0

for i in range(2, num+1):
    if len(prime_factorization(i)) == 2:
        count += 1

print(count)
