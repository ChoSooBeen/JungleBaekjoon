import sys

N, M = map(int, sys.stdin.readline().split())
small = [int(sys.stdin.readline()) for _ in range(M)]

# 만약 막히지 않고 속도가 계속 증가하면 가능한 속도
max_speed = int((2*N)**(1/2)) + 1

# dp[i][j] = i 속도로 j번 돌로 온 최소 횟수
dp = [[float('inf')] * (max_speed+1) for _ in range(N+1)]

# 문제 조건 상 무조건 2번에 처음 움직여야하는데
# 2번 돌이 너무 작으면 애초에 이동 불가능
if 2 not in small :
    dp[2][1] = 1 # 기저값
    for num in range(3, N+1) : #3번 돌부터
        if num not in small : # 올라갈 수 있는 돌이면
            for speed in range(1, max_speed) :
                # 1. num-speed = 전 위치
                # 2. 각각 현재 속도의 -1, 0, +1 만큼의 이동 횟수를 가져온다.
                # 3. 가장 작은 값에 +1
                dp[num][speed] = min(dp[num - speed][speed - 1], dp[num - speed][speed], dp[num - speed][speed + 1]) + 1

ans = min(dp[N])
if ans == float('inf') : # 도달 못함
    print(-1)
else :
    print(ans)