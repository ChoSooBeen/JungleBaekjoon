import sys
import heapq

n = int(sys.stdin.readline())

# 0 : 검은방(갈 수 없음) 1 : 흰방
miro = [list(sys.stdin.readline()) for _ in range(n)]

def dijkstra(x, y) :
    visited = [[0]*n for _ in range(n)]
    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = 1
    heapq.heappush(queue, (visited[x][y], x, y))
    
    while queue :
        # 최소 비용을 갖는 경로부터 확인한다.
        cur_cost, curX, curY = heapq.heappop(queue)
        for i in range(4) :
            nx, ny = curX + dx[i], curY + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if miro[nx][ny] == '1': # 흰방이면 비용이 증가할 필요가 없다.
                    visited[nx][ny] = cur_cost
                else : # 검은방이면 비용을 1 증가시켜야 한다.
                    visited[nx][ny] = cur_cost+1
                heapq.heappush(queue, (visited[nx][ny], nx, ny))
    return visited[n-1][n-1]-1 # 1부터 시작하여 마지막에 1 빼주기
    
print(dijkstra(0, 0))



########################## BFS를 이용한 풀이 ########################
# import sys
# from collections import deque

# n = int(sys.stdin.readline())

# # 0 : 검은방(갈 수 없음) 1 : 흰방
# miro = [list(sys.stdin.readline()) for _ in range(n)]

# def bfs(x, y) :
#     visited = [[0]*n for _ in range(n)]
#     queue = deque()
    
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     visited[x][y] = 1
#     queue.append((x, y))
    
#     while queue :
#         curX, curY = queue.popleft()
#         for i in range(4) :
#             nx, ny = curX + dx[i], curY + dy[i]
#             if 0 <= nx < n and 0 <= ny < n :
#                 if visited[nx][ny] == 0 :
#                     if miro[nx][ny] == '1' :
#                         visited[nx][ny] = visited[curX][curY]
#                         queue.appendleft((nx, ny))
#                     else :
#                         visited[nx][ny] = visited[curX][curY]+1
#                         queue.append((nx, ny))
#     return visited[n-1][n-1]-1

# print(bfs(0,0))