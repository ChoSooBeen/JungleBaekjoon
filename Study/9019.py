import sys
from collections import deque

def bfs(a, b) :
    queue = deque()
    visited = {}
    
    queue.append((a, ''))
    visited[a] = 1
    
    while queue :
        num, result = queue.popleft()
        if num == b :
            print(result)
            return
        d = (2 * num) % 10000
        if d not in visited :
            queue.append((d, result+'D'))
            visited[num] = 1
        s = (num-1) % 10000
        if s not in visited :
            queue.append((s, result+'S'))
            visited[s] = 1
        l = num // 1000 + (num % 1000) * 10
        if l not in visited :
            queue.append((l, result+'L'))
            visited[l] = 1
        r = num // 10 + (num % 10) * 1000
        if r not in visited :
            queue.append((r, result+'R'))
            visited[r] = 1

t = int(sys.stdin.readline())
for _ in range(t) :
    a, b = map(int, sys.stdin.readline().strip().split())
    bfs(a, b)