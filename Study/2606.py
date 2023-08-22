import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
queue = deque()

queue.append(1)
visited[1] = True

count = 0
while queue :
    cur = queue.popleft()
    for connect in graph[cur] :
        if visited[connect] == False :
            queue.append(connect)
            visited[connect] = True
            count += 1
print(count)