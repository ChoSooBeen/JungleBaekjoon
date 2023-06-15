import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(height) :
    queue = deque()
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] and graph[i][j] > height :
                count += 1
                queue.append((i, j))
                visited[i][j] = True
                while queue :
                    cx, cy = queue.popleft()
                    for k in range(4) :
                        nx, ny = cx + dx[k], cy + dy[k]
                        if nx >= 0 and nx < N and ny >= 0 and ny < N :
                            if not visited[nx][ny] and graph[nx][ny] > height :
                                queue.append((nx, ny))
                                visited[nx][ny] = True 
    return count        

result = 0
for h in range(101) :
    t = bfs(h)
    result = max(result, t)
    if t == 0 :
        break
print(result)