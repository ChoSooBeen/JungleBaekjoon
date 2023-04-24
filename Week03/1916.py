import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N)]
for _ in range(M) :
    s, e, w = map(int, sys.stdin.readline().split())
    bus[s-1].append((e-1, w))
    
start, end = map(int, sys.stdin.readline().split())

def dijkstra(start, end) :
    # start를 시작으로 각 정점까지의 최단 거리 저장
    distance = [float('inf')] * N
    queue = []
    
    distance[start] = 0 # 시작점 거리 0으로  초기화
    heapq.heappush(queue, (distance[start], start))
    
    while queue :
        cur_dis, cur_idx = heapq.heappop(queue)
        # 현재 거리가 출발지부터 현재까지의 거리보다 작거나 같을 경우
        # 같은야 하는 이유는 처음에는 cur_dis와 distance[cur_idx]가 같을 수 밖에 없다.
        # 기존의 거리보다 더 짧은 값이 나타날 경우
        if cur_dis <= distance[cur_idx] :
            for idx, weight in bus[cur_idx] :
                # 간선 완화 과정
                # 지금까지 발견된 최단 거리보다 idx 노드를 통해 가는 길이 더 짧을 경우
                # 최단 거리 갱신
                if cur_dis + weight < distance[idx] :
                    distance[idx] = cur_dis + weight
                    heapq.heappush(queue, (distance[idx], idx))
    return distance[end]
    
print(dijkstra(start-1, end-1))