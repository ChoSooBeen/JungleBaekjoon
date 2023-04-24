import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

visited = [[[0]*M for _ in range(N)] for _ in range(H)]
def bfs() :
    while queue :
        curX, curY, curH = queue.popleft()
        for i in range(6) :
            nx, ny, nh = curX + dx[i], curY + dy[i], curH + dh[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H :
                if visited[nh][nx][ny] == 0 and tomato[nh][nx][ny] == 0 :
                    tomato[nh][nx][ny] = tomato[curH][curX][curY] + 1
                    visited[nh][nx][ny] = 1
                    queue.append((nx, ny, nh))

def getDay() :
    day = 0
    for i in range(H) : # 높이
        for j in range(N) : # 행
            for k in range(M) : # 열
                if tomato[i][j][k] == 0 : # 안 익은 토마토 존재
                    print(-1)
                    return
                if day < tomato[i][j][k] :
                    day = tomato[i][j][k]
    if day > 0 : 
        day -= 1  #1부터 시작했기 때문에 1 빼주기    
    print(day)

queue = deque()     
for i in range(H) : # 높이
    for j in range(N) : # 행
        for k in range(M) : # 열
            if visited[i][j][k] == 0 and tomato[i][j][k] == 1 :
                queue.append((j, k, i)) # 처음부터 1로 시작하는 모든 경우 큐에 삽입
                visited[i][j][k] = 1

bfs()
getDay()