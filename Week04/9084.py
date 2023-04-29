import sys

T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    
    dp = [0] * (M+1) # 각각의 금액에 대한 동전으로 만들 모든 방법의 수 저장
    dp[0] = 1 # 기저 값으로 지정
    for c in coin :
        for i in range(1, M+1) :
            if i >= c :
                dp[i] += dp[i-c]
    print(dp[M])