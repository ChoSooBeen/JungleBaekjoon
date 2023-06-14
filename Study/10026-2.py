import sys
from collections import deque

N = int(sys.stdin.readline())
pic = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue :
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N :
                if not visited[nx][ny] and pic[cx][cy] == pic[nx][ny] :
                    queue.append((nx, ny))
                    visited[nx][ny] = True         
    
def red_green(x, y) :
    queue = deque() 
    queue.append((x, y))
    rg_visited[x][y] = True
    
    while queue :
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N :
                if not rg_visited[nx][ny] :
                    if pic[cx][cy] == pic[nx][ny] or (pic[cx][cy] != 'B' and pic[nx][ny] != 'B') :
                        queue.append((nx, ny))
                        rg_visited[nx][ny] = True 

visited = [[False] * N for _ in range(N)]
rg_visited = [[False] * N for _ in range(N)]
count = 0
rg_count = 0
for i in range(N) :
    for j in range(N) :
        if not visited[i][j] :
            bfs(i, j)
            count += 1
        if not rg_visited[i][j] :
            red_green(i, j)
            rg_count += 1
print(count, rg_count)