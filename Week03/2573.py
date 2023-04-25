import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빙산 녹이는 함수
def melting() :
    change = []
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if iceberg[i][j] != 0 :
                sea = 0 # 현재 위치에서 0과 맞닿아 있는 개수
                for k in range(4) :
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] == 0 :
                        sea += 1
                if iceberg[i][j] - sea > 0 : # 아직 녹아서 사라지지 않을 경우
                    iceberg[i][j] = iceberg[i][j] - sea
                else : # 녹아서 사라질 경우 후에 계산을 위해 나중에 변경
                    change.append((i, j))
    for x, y in change : # 사라질 부분 0으로 변경
        iceberg[x][y] = 0      

def bfs(s, e) :
    queue = deque()
    
    queue.append((s, e))
    visited[s][e] = 1
    
    while queue :
        xx, yy = queue.popleft()
        for i in range(4) :
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and iceberg[nx][ny] != 0 :
                visited[nx][ny] = 1
                queue.append((nx, ny))

day = 0
while True :
    visited = [[0] * M for _ in range(N)]
    count = 0 # 현재 빙산 덩어리의 개수
    for i in range(1, N-1) :
        for j in range(1, M-1) :
            if iceberg[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    if count > 1 : # 이미 나눠져 있다면
        print(day)
        break
    elif count == 0 : # 이미 녹아서 사라졌다면
        print(0)
        break
    
    # 아직 한덩어리라면 더 녹여본다.
    melting()
    day += 1

###################### DFS를 이용한 풀이 ################################
# import sys

# N, M = map(int, sys.stdin.readline().split())

# iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 빙산 녹이는 함수
# def melting() :
#     change = []
#     for i in range(1, N-1) :
#         for j in range(1, M-1) :
#             if iceberg[i][j] != 0 :
#                 sea = 0 # 현재 위치에서 0과 맞닿아 있는 개수
#                 for k in range(4) :
#                     nx, ny = i + dx[k], j + dy[k]
#                     if 0 <= nx < N and 0 <= ny < M and iceberg[nx][ny] == 0 :
#                         sea += 1
#                 if iceberg[i][j] - sea > 0 : # 아직 녹아서 사라지지 않을 경우
#                     iceberg[i][j] = iceberg[i][j] - sea
#                 else : # 녹아서 사라질 경우 후에 계산을 위해 나중에 변경
#                     change.append((i, j))
#     for x, y in change : # 사라질 부분 0으로 변경
#         iceberg[x][y] = 0

# # 빙산 덩이리 탐색을 위한 DFS 함수
# def dfs(s, e) :
#     visited[s][e] = 1
#     stack = [(s, e)]
    
#     while stack :
#         xx, yy = stack.pop()
#         for i in range(4) :
#             nx, ny = xx + dx[i], yy + dy[i]
#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and iceberg[nx][ny] != 0:
#                 visited[nx][ny] = 1
#                 stack.append((nx, ny))

# day = 0
# while True :
#     visited = [[0] * M for _ in range(N)]
#     count = 0 # 현재 빙산 덩어리의 개수
#     for i in range(1, N-1) :
#         for j in range(1, M-1) :
#             if iceberg[i][j] != 0 and visited[i][j] == 0:
#                 dfs(i, j)
#                 count += 1
#     if count > 1 : # 이미 나눠져 있다면
#         print(day)
#         break
#     elif count == 0 : # 이미 녹아서 사라졌다면
#         print(0)
#         break
    
#     # 아직 한덩어리라면 더 녹여본다.
#     melting()
#     day += 1