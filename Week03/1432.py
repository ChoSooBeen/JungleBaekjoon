import sys
import heapq

N = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
degree = [0] * N
graph = [[] for _ in range(N)]

# 후에 사전적 정렬을 하기 위해 진출차수(Out Degree) 사용
for i in range(N) :
    for j in range(N) :
        if matrix[i][j] == '1' :
            # 입력된 값을 뒤집어서 새로 저장
            graph[j].append(i)
            degree[i] += 1

def topologySort() :
    queue = []
    result = [0] * N
    idx = N
    
    # 진출 차수가 존재하지 않는 경우 -> 노드 번호가 크다.
    for i in range(N) :
        if degree[i] == 0 :
            # 최대힙으로 저장
            heapq.heappush(queue, -i)
    
    while queue :
        # 현재 최대힙 안에서 우선순위가 가장 큰 노드를 pop
        # 같은 조건을 가진 노드 1, 2가 있다면 위상 정렬 후에도 3, 4와 같이 순서가 맞아야한다.
        cur = heapq.heappop(queue)
        result[-cur] = idx
        idx -= 1
        for i in graph[-cur] :
            degree[i] -= 1
            if degree[i] == 0 :
                heapq.heappush(queue, -i)
    # 만약 result[i] = 0 이라는 의미는 한번도 힙에 들어간적이 없다는 의미로 
    # 사이클이 존재하면 나타난다.
    if result.count(0) > 0 : 
        print(-1)
    else :
        print(*result)
    
topologySort()