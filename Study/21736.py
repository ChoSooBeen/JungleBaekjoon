import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
campus = [list(sys.stdin.readline().strip()) for _ in range(n)]

def bfs(x, y, n, m, campus) :
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    
    queue.append((x, y))
    visited[x][y] = True
    
    while queue :
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m :
                if visited[nx][ny] == False and campus[nx][ny] != 'X' :
                    if campus[nx][ny] == 'P' :
                        count += 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    print(count if count != 0 else 'TT')

for i in range(n) :
    for j in range(m) :
        if campus[i][j] == 'I' :
            bfs(i, j, n, m, campus)
            break