import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline()) # 시작 정점
graph = [[] for _  in range(v+1)]

for _ in range(e) :
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))

def dijkstra(graph, s, v) :
    distance = [sys.maxsize] * (v+1)
    queue = []
    
    distance[s] = 0
    heapq.heappush(queue, [distance[s], s])
    
    while queue :
        dist, vertext = heapq.heappop(queue)
        
        if distance[vertext] >= dist :
            for nv, w in graph[vertext] :
                if distance[nv] > dist + w :
                    distance[nv] = dist + w
                    heapq.heappush(queue, [distance[nv], nv])
    
    for i in range(1, v+1) :
        if distance[i] == sys.maxsize :
            print("INF")
        else :
            print(distance[i])

dijkstra(graph, k, v)