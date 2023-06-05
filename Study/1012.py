import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
    queue = deque()
    count = 0
    
    for i in range(M) :
        for j in range(N) :
            if array[i][j] == 1 and visited[i][j] == False :
                visited[i][j] = True
                queue.append((i, j))
                while queue :
                    currx, curry = queue.popleft()
                    for k in range(4) :
                        nx, ny = currx + dx[k], curry + dy[k]
                        if nx >= 0 and nx < M and ny >= 0 and ny < N :
                            if array[nx][ny] == 1 and visited[nx][ny] == False :
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                count += 1
    return count

for _ in range(T) :
    M, N, K = map(int, sys.stdin.readline().split())
    visited = [[False] * N for _ in range(M)]
    array = [[0] * N for _ in range(M)]
    for _ in range(K) :
        x, y = map(int, sys.stdin.readline().split())
        array[x][y] = 1
    print(bfs())