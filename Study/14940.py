import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 2 :
            result[i][j] = 0
            queue.append((i, j))
        elif graph[i][j] == 0 :
            result[i][j] = 0
   
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  

while queue :
    cx, cy = queue.popleft()
    for i in range(4) :
        nx, ny = cx + dx[i], cy + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if graph[nx][ny] == 1 and result[nx][ny] == -1 :
                queue.append((nx, ny))
                result[nx][ny] = result[cx][cy] + 1

for i in range(n) :
    for j in range(m) :
        print(result[i][j], end=" ")
    print()