import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix = [[0] * N for _ in range(N)]
visited = [0] * N
count = 0

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    # 양방향 그래프
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

# BFS로 탐색
def connection(v) :
    global count
    queue = deque()
    
    queue.append(v)
    visited[v] = 1
    
    while queue :
        cur = queue.popleft()

        for i in range(N) :
            if matrix[i][cur] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
    # 시작 정점 v에서 연결된 모든 정점 탐색이 끝나면 coun++
    count += 1

for i in range(N) :
    if visited[i] == 0 :
        connection(i)

print(count)