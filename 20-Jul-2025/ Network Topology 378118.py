# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict


n, m = map(int, input().split())

dg = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    dg[a-1] += 1
    dg[b-1] += 1

if m > n:
    print("unknown topology")

elif n == m:
    if dg.count(2) == m:
        print("ring topology")
    else:
        print("unknown topology")

elif n == m +1:
    if 1 == dg.count(m) and dg.count(1) == m:
        print("star topology")
    elif dg.count(1) == 2:
        print("bus topology")
    else:
        print("unknown topology")
else:
    print("unknown topology")