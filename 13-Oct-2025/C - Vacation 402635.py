# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

dp = []
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    dp.append(nums)


for i in range(n - 2, -1, -1):
    dp[i][0]  += max(dp[i+1][1], dp[i+1][2])
    dp[i][1]  += max(dp[i+1][0], dp[i+1][2])
    dp[i][2]  += max(dp[i+1][1], dp[i+1][0])

print(max([dp[0][i] for i in range(3)]))