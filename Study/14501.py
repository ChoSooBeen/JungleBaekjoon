import sys

n = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n+1)
    
for i in range(n-1, -1, -1) :
    if i + works[i][0] <= n :
        dp[i] = max(dp[i+1], dp[i + works[i][0]] + works[i][1])
    else :
        dp[i] = dp[i+1]

print(dp[0])