import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited_broken = [[0] * M for _ in range(N)]

def bfs() :
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print_flag = True
    
    visited[0][0] = 1
    visited_broken[0][0] = 1
    queue.append((0,0, False))
    
    while queue :
        cx, cy, flag = queue.popleft()
        if cx == N-1 and cy == M-1 :
            result = max(visited[cx][cy], visited_broken[cx][cy])
            print(result)
            print_flag = False
            break
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M :
                if flag == True : #이미 한번 부쉈을 경우
                    if graph[nx][ny] == '0' and visited_broken[nx][ny] == 0 :
                        queue.append((nx, ny, flag))
                        visited_broken[nx][ny] = visited_broken[cx][cy] + 1
                else : #한번도 안 부순 경우
                    if graph[nx][ny] == '0' and visited[nx][ny] == 0 :
                        queue.append((nx, ny, flag))
                        visited[nx][ny] = visited[cx][cy] + 1
                    elif graph[nx][ny] == '1' and visited_broken[nx][ny] == 0 :
                        queue.append((nx, ny, True))
                        visited_broken[nx][ny] = visited[cx][cy] + 1
    if print_flag :
        print(-1)
bfs()