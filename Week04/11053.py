import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = 1 # 기저값
for i in range(1, N) :
    t = 0 # 현재 A[i]의 값보다 작은 값들 중 가장 큰 값의 dp 저장
    for j in range(i) :
        if A[i] > A[j] and t < dp[j] :
            t = dp[j]
    dp[i] = t + 1

print(max(dp))