import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(m) :
    s, e, t = map(int, sys.stdin.readline().split())
    roads[s].append([e, t])
    
def dijkstra(graph, s, v) :
    queue = []
    
    distance[s][s] = 0
    heapq.heappush(queue, [distance[s][s], s])
    
    while queue :
        dist, vertext = heapq.heappop(queue)
        
        if distance[s][vertext] >= dist :
            for nv, w in graph[vertext] :
                if distance[s][nv] > dist + w :
                    distance[s][nv] = dist + w
                    heapq.heappush(queue, [distance[s][nv], nv])

for i in range(1, n+1) :
    dijkstra(roads, i, n)

result = 0
for i in range(1, n+1) :
    if result < distance[i][x] + distance[x][i] :
        result = distance[i][x] + distance[x][i]
print(result)