import sys
import heapq
import collections

V, E = map(int, sys.stdin.readline().split())
matrix = collections.defaultdict(list) # 빈 리스트 생성
for _ in range(E) :
    x, y, weight = map(int, sys.stdin.readline().split())
    # 무방향 그래프 표현
    # 0번 부터 V-1번까지 노드라고 생각한다.(문제상에는 1 ~ V 까지)
    matrix[x-1].append([weight, x-1, y-1])
    matrix[y-1].append([weight, y-1, x-1])

def primMST(v) :
    node = [0] * V # 방문 여부를 저장할 배열
    # 시작 정점 방문
    node[v] = 1
    # 시작노드에서 갈 수 있는 모든 간선 리스트
    candidate = matrix[v] 
    heapq.heapify(candidate) # 우선순위 큐로 변환
    sum = 0
    while candidate :
        weight, x, y = heapq.heappop(candidate)
        # 정점 y를 방문한 적이 없다면
        if node[y] == 0 :
            node[y] = 1
            sum += weight
            
            # y에서 갈 수 있는 모든 간선에 대한 정보 중에서
            # 방문한 적이 없는 노드들만 candidate에 저장
            for edge in matrix[y] :
                if node[edge[2]] == 0 :
                    heapq.heappush(candidate, edge)
    print(sum)

primMST(0)
    

################### 크루스칼 알고리즘 구현#########################################
# import sys

# V, E = map(int, sys.stdin.readline().split())

# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
# matrix.sort(key= lambda x : x[2])

# # 각 정점의 부모노드를 자기 자신으로 설정
# # make_set() 동작이라고 생각하면된다.
# disjoint = [i for i in range(V+1)]

# # x의 부모노드 찾기
# # 주의할 점은 부모노드가 자기 자신이 아니면 그 부모 노드의 부모 노드를 찾아가야 한다.!!
# def find_set(x) :
#     if disjoint[x] == x :
#         return x
#     else :
#         return find_set(disjoint[x])

# # x, y의 부모 노드를 통일시킨다.
# # 단, 작은 값으로 통일
# def union_set(x, y) :
#     a = find_set(x)
#     b = find_set(y)
#     if a < b :
#         disjoint[b] = a
#     else :
#         disjoint[a] = b
    
    
# sum = 0
# # 크루스칼 알고리즘 사용!
# for x, y, weight in matrix :
#     if find_set(x) != find_set(y) :
#         union_set(x, y)
#         sum += weight

# print(sum)
