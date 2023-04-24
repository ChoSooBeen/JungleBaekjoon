import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
# 중복 제거를 위해 set 사용
coin = list(set(int(sys.stdin.readline()) for _ in range(n)))
coin.sort()

queue = deque()
for c in coin :
    # (현재 코인의 값, 만드는데 쓰인 동전 개수)
    # 구해야 할 값보다 작은 것만 저장
    if c <= k :
        queue.append((c, 1))

def bfs() :
    # 인덱스 = cost 즉, 인덱스만큼의 가치를 가진 동전의 최소 개수를 이미 찾았다.
    visited = [0] * (k+1)
    while queue :
        cost, count = queue.popleft()
        # 원하는 가치를 가진 값이 등장하면 바로 반환
        if cost == k :
            return count
        for c in coin :
            # k보다 작거나 같고 아직 최소 개수를 찾지 못했으면
            if cost + c <= k and visited[cost+c] == 0 :
                visited[cost+c] = 1
                queue.append((cost+c, count + 1))
    return -1 # 결국 못찾았으면

print(bfs())