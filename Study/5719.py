import sys
from collections import deque
import heapq

n, k = map(int, sys.stdin.readline().split())

# 다익스트라 알고리즘을 사용한 풀이
def dijkstra(start, end) :
    times = [sys.maxsize] * 100001
    heap = []
    
    times[start] = 0
    heapq.heappush(heap, [times[start], start])
    
    while heap :
        t, v = heapq.heappop(heap)
        for n in [v + 1, v - 1, v * 2] :
            if n >= 0 and n <= 100000 :
                if n == v * 2 and times[n] > t :
                    times[n] = t
                    heapq.heappush(heap, [times[n], n])
                elif times[n] > t + 1 :
                    times[n] = t + 1
                    heapq.heappush(heap, [times[n], n])
    print(times[end])
dijkstra(n, k)
  
# BFS를 이용한 풀이              
def BFS(start, end) :
    times = [sys.maxsize] * 100001
    queue = deque()
    
    times[start] = 0
    queue.append(start)
    
    while queue :
        current = queue.popleft()
        
        for n in [current + 1, current - 1, current * 2] :
            if n >= 0 and n <= 100000 :
                if n == current * 2 and times[n] > times[current] :
                    times[n] = times[current]
                    queue.append(n)
                elif times[n] > times[current] + 1 :
                    times[n] = times[current] + 1
                    queue.append(n)
    print(times[end])
BFS(n, k)