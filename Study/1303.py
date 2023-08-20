import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
white = 0
blue = 0

def bfs(x, y) :
    global white, blue
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    color = graph[x][y]
    count = 1
    
    while queue :
        curX, curY = queue.popleft()
        for i in range(4) :
            nx, ny = curX + dx[i], curY + dy[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N :
                if graph[nx][ny] == color and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    if color == 'W' :
        white += count**2
    else :
        blue += count**2

for i in range(M) :
    for j in range(N) :
        if not visited[i][j] :
            bfs(i, j)
print(white, blue)