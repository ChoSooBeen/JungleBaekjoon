import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    
    while queue : 
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < H and ny >= 0 and ny < W :
                if grid[nx][ny] == '#' and not visited[nx][ny] :
                    queue.append((nx, ny))
                    visited[nx][ny] = True

for _ in range(T) :
    H, W = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    count = 0
    for i in range(H) :
        for j in range(W) :
            if grid[i][j] == '#' and not visited[i][j] :
                count += 1
                bfs(i, j)
    print(count)