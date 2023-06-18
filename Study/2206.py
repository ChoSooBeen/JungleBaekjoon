import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs() :
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[0][0] = 1
    queue.append((0,0, False))
    
    while queue :
        cx, cy, flag = queue.popleft()
        if cx == N-1 and cy == M-1 :
            break
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M :
                if visited[nx][ny] == 0 :
                    if graph[nx][ny] == '0' :
                        queue.appendleft((nx, ny, flag))
                        visited[nx][ny] = visited[cx][cy] + 1
                    elif graph[nx][ny] == '1' and not flag :
                        queue.append((nx, ny, True))
                        visited[nx][ny] = visited[cx][cy] + 1
    if visited[N-1][M-1] == 0 :
        print(-1)
    else :
        print(visited[N-1][M-1])
bfs()