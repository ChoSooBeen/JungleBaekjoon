import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

color_count = 0    
color_weakness = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) : #색약이 아닌 사람이 보는 구역
    global color_count, color_weakness
    queue = deque()
    
    visited[x][y] = 1
    queue.append((x,y))
    
    while queue :
        curx, cury = queue.popleft()
        for i in range(4) :
            nx, ny = curx + dx[i], cury + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < N and visited[nx][ny] == 0 and graph[curx][cury] == graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

def weak_bfs(x, y) : #적록색약인 사람이 보는 구역
    global color_count, color_weakness
    queue = deque()
    
    weak_visited[x][y] = 1
    queue.append((x,y))
    
    flag = True # True일 경우 R,G 탐색
    if graph[x][y] == 'B' :
        flag = False
        
    while queue :
        curx, cury = queue.popleft()
        for i in range(4) :
            nx, ny = curx + dx[i], cury + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < N and weak_visited[nx][ny] == 0 :
                if flag and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                    queue.append((nx, ny))
                    weak_visited[nx][ny] = 1
                elif not flag and graph[nx][ny] == 'B' :
                    queue.append((nx, ny))
                    weak_visited[nx][ny] = 1


visited = [[0]*N for _ in range(N)]
weak_visited = [[0]*N for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if visited[i][j] == 0 :
            bfs(i, j)
            color_count += 1
        if weak_visited[i][j] == 0 :
            weak_bfs(i, j)
            color_weakness += 1            
        
print(color_count, color_weakness)