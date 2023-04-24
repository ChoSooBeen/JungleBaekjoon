import sys
from collections import deque

N, M = map(int ,sys.stdin.readline().split())

miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def bfs(miro) :
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    
    queue.append((0,0))
    visited[0][0] = 1
    
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    
    while queue :
        curX, curY = queue.popleft()
        for i in range(4) :
            nX, nY = curX + x[i], curY + y[i]
            if 0 <= nX < N and 0 <= nY < M :
                if visited[nX][nY] == 0 and miro[nX][nY] == 1 :
                    miro[nX][nY] = miro[curX][curY] + 1
                    visited[nX][nY] = 1
                    queue.append((nX, nY))
    print(miro[N-1][M-1])

bfs(miro)