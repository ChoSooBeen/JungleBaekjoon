import sys

N, K = map(int, sys.stdin.readline().split())
# 오름차순으로 입력을 받는다.
coin = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
# 동전의 가치가 가장 큰 동전부터 반복 시작
for i in range(N-1, -1, -1) :
    if K == 0 :
        break
    # 현재 K보다 작은 수 중 가장 큰 수를 선택하여 계산
    if coin[i] <= K :
        count += K//coin[i]
        K %= coin[i]

print(count)