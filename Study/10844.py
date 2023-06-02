import sys

# https://cotak.tistory.com/12 참고

N = int(sys.stdin.readline())

# 행 : 자리수
# 열 : 앞에 오는 수
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10) :
    dp[1][i] = 1

for i in range(2, N+1) :
    dp[i][0] = dp[i-1][1] # 앞자리 0일 경우 -> 1만 가능
    for j in range(1, 9) : # 앞자리 1 ~ 8일 경우 -> +1, -1씩 가능
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8] # 앞자리 9일 경우 -> 8만 가능

print(sum(dp[N]) % 1000000000)