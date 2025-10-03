# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())

heights = list(map(int, input().split()))

heights.append(float("inf"))
dp = [0] * n + [float('inf')]

for i in range(n-2, -1, -1):
    dp[i] = min([dp[i+1] + abs(heights[i+1] - heights[i]), dp[i+2] + abs(heights[i+2] - heights[i])])

print(dp[0])