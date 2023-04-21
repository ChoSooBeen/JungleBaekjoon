import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0]*N for _ in range(N)]

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

def dfs(v) :
    visited = [0] * N
    stack = []
    result = []
    
    stack.append(v)
    visited[v] = 1
    result.append(v+1)
    
    while stack :
        cur = stack[-1]
        flag = False
        for i in range(N) :
            if matrix[cur][i] == 1 and visited[i] == 0 :
                stack.append(i)
                visited[i] = 1
                result.append(i+1)
                flag = True
                break
        if not flag :
            stack.pop()
    print(*result)
    
def bfs(v) :
    visited = [0] * N
    queue = deque()
    result = []
    
    queue.append(v)
    visited[v] = 1
    result.append(v+1)
    
    while queue :
        cur = queue.popleft()

        for i in range(N) :
            if matrix[i][cur] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
                result.append(i+1)
    print(*result)
    
dfs(V-1)
bfs(V-1)