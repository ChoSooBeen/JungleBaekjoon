import sys

N = int(sys.stdin.readline())
# matrix[i][0] : i번째 행렬의 행의 수 / matrix[i][1] : i번째 행렬의 열의 수
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[i][j] = Ai...j 행렬의 최소 연산 횟수
dp = [[0] * N for _ in range(N)]

# l : 행렬 체인 길이 (행렬은 최소 1개)
for l in range(1, N) :
    for i in range(N-l): # 행렬 곱셈의 시작 행렬 인덱스
        j = i+l # 행렬 곱셈의 끝 행렬 인덱스
        dp[i][j] = float('inf')
        for k in range(i, j) : # i ~ j 사이를 k로 나눈다.
            q = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k+1][0] * matrix[j][1]
            if q < dp[i][j] :
                dp[i][j] = q

# 첫번째 행렬부터 마지막 행렬까지의 최소 연산 횟수
print(dp[0][N-1])