import sys
from collections import deque
import copy

def wall(count) :
    if count == 3 :
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                graph[i][j] = 1
                wall(count + 1)
                graph[i][j] = 0

def bfs() :
    queue = deque()
    copy_graph = copy.deepcopy(graph)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n) :
        for j in range(m) :
            if copy_graph[i][j] == 2 :
                queue.append((i, j))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m :
                if copy_graph[nx][ny] == 0 :
                    copy_graph[nx][ny] = 2
                    queue.append((nx, ny))
    zero_count(copy_graph)
    
def zero_count(grp) :
    global result
    count = 0
    for i in range(n) :
        for j in range(m) :
            if grp[i][j] == 0 :
                count += 1
    result = max(result, count)

if __name__ == '__main__' :
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    wall(0)
    print(result)