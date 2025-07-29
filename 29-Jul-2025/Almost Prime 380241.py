# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

num = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, num//2 + 1):
    if is_prime(i):
        primes.append(i)

count = 0
m = len(primes)
for i in range(2,num+1):
    div = 0
    for j in range(m):
        if i % primes[j] == 0:
            div += 1
    if div == 2:
        count += 1
print(count)