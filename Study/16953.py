import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

def bfs(start, end) :
    visited = {}
    queue = deque()
    
    queue.append(start)
    visited[start] = 0
    
    while queue :
        current = queue.popleft()
        x, y = 2 * current, 10 * current + 1
        if x <= end and x not in visited :
            queue.append(x)
            visited[x] = visited[current] + 1
        if y <= end and y not in visited :
            queue.append(y)
            visited[y] = visited[current] + 1
    if end not in visited :
        print(-1)
    else :
        print(visited[end] + 1)

bfs(a, b)