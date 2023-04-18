import sys
import heapq

N = int(sys.stdin.readline())

min_heap = [] # 중간값보다 작은 값들이 들어갈 우선순위 큐 - 최대힙
max_heap = [] # 중간값보다 큰 값들이 들어갈 우선순위 큐 - 최소힙
for _ in range(N) :
    num = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap) :
        heapq.heappush(min_heap, -num) # 최대힙으로 사용하기 위해 값에 - 사용
    else :
        heapq.heappush(max_heap, num)
    # 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수
    # 즉, min_heap이 중간값을 가지고 있도록 해야한다.
    if max_heap and max_heap[0] < -min_heap[0] :
         left = heapq.heappop(min_heap)
         right = heapq.heappop(max_heap)
         heapq.heappush(min_heap, -right)
         heapq.heappush(max_heap, -left)
    print(-min_heap[0])