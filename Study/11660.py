import sys

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적합을 저장할 이차원 배열
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1) :
    for j in range(1, N+1) :
        dp[i][j] = table[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# 원하는 구간합 구하기
for _ in range(M) :
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    sum = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(sum)