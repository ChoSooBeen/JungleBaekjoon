import sys

n = int(sys.stdin.readline())
wines = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * n
dp[0] = wines[0]
if n > 1 :
    dp[1] = wines[0] + wines[1]
if n > 2 :
    dp[2] = max(dp[1], wines[0] + wines[2], wines[1] + wines[2])
for i in range(3, n) :
    dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i] + wines[i-1], dp[i-1])
print(dp[n-1])