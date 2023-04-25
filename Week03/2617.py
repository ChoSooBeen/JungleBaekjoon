import sys

N, M = map(int, sys.stdin.readline().split())
mid = (N+1) // 2 # 중앙값의 인덱스
marble = [[0] * N for _ in range(N)]
for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    # x가 y보다 무겁다.
    marble[x-1][y-1] = 1

# 플로이드-워셜 알고리즘
# 만약 무게를 i가 k보다 무겁고 k가 j보다 무겁다는 것을 알면
# i 는 j 보다 무겁다고 할 수 있다.
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if marble[i][k] and marble[k][j] :
                marble[i][j] = 1

result = 0
for i in range(N) :
    # i 보다 가벼운 구슬의 개수를 저장할 변수 left
    # i 보다 무거운 구슬의 개수를 저장할 변수 right
    left, right = 0, 0
    for j in range(N) :
        if i == j :
            continue
        elif marble[i][j] == 1 :
            left += 1
        elif marble[j][i] == 1 :
            right += 1
    if left >= mid or right >= mid :
        result += 1
print(result)
                
###################### DFS를 이용한 풀이 #######################################
# import sys

# N, M = map(int, sys.stdin.readline().split())

# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# heavy = [[]for _ in range(N)]
# light = [[]for _ in range(N)]

# mid = (N+1) // 2 # 중앙값의 인덱스

# # 각각의 구슬이 무거운, 가변운 측정 결과 저장
# for x, y in arr :
#     # x보다 가벼운 구슬들
#     light[x-1].append(y-1)
#     # y보다 무거운 구슬들
#     heavy[y-1].append(x-1)

# def dfs(v, weight) :
#     visited = [0] * N
#     stack = []
    
#     visited[v] = 1
#     stack.extend(weight[v])
#     count = 0
    
#     while stack :
#         current = stack.pop()
#         if visited[current] == 0 :
#             count += 1
#             stack.extend(weight[current])
#             visited[current] = 1
#     return count

# result = 0
# for i in range(N) :
#     h = dfs(i, heavy) # 현재 구슬보다 무거운 구슬 개수
#     l = dfs(i, light) # 현재 구슬보다 무겁지 않은 구슬 개수
#     if h >= mid or l >= mid :
#         result += 1
# print(result)