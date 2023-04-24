import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)

result = []

def bfs(x):
    visited = [sys.maxsize] * N
    queue = deque()
    
    visited[x] = 0
    queue.append(x)
    
    while queue :
        cur = queue.popleft()
        for i in graph[cur] :
            if visited[i] == sys.maxsize :
                visited[i] = visited[cur] + 1
                queue.append(i)
                if visited[i] == K :
                    result.append(i+1)

bfs(X-1)
if len(result) == 0 :
    print(-1)
else :
    result.sort() # 결과를 오름차순으로 출력!!
    for i in result :
        print(i)