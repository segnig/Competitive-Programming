# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

n, k= map(int, input().split())

heights = list(map(int, input().split()))

heights.append(float("inf"))
dp = [0] * n + [float('inf')]

for i in range(n-2, -1, -1):
    result = float("inf")
    for j in range(k, 0, -1):
        if i + j < len(heights):
            result = min(result, dp[i+j] + abs(heights[i+j] - heights[i]))
    dp[i] = result

print(dp[0])