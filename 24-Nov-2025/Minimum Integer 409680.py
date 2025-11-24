# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

for _ in range(int(input())):
    l, r, d = map(int, input().split())

    if l > d:
        print(d)
    else:
        m = r % d

        if m == 0:
            print(r + d)
        else:
            print((r // d + 1) * d)