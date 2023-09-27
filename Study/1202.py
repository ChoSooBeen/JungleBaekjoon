import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

bags.sort()
jewels.sort()

result = 0
weight = []
for i in range(k) :
    while jewels and jewels[0][0] <= bags[i] :
        heapq.heappush(weight, -jewels[0][1])
        heapq.heappop(jewels)
    if weight :
        result -= heapq.heappop(weight)

print(result)