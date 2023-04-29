import sys

N, K = map(int, sys.stdin.readline().split())

# dp[i][j] = i번째 가방까지 가능하고 j 용량일 때 최대 가치
dp = [[0] * (K+1) for _ in range(N+1)]
# obj[0] = 무게 / obj[1] = 가치
obj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N+1) :
    w, v = obj[i-1]
    for j in range(1, K+1) :
        # 가능한 용량 j보다 현재 물건의 용량이 클 경우
        if w > j :
            dp[i][j] = dp[i-1][j]
        # 작을 경우
        # 1. 전의 물건을 넣었을 경우
        # 2. 현재 물건을 넣고 나머지 용량에 대한 가치를 더한 경우
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)       
             
print(dp[N][K])