import sys

# https://woonys.tistory.com/entry/정글사관학교-22일차-TIL-아침-산책with-Python-위상-정렬-알고리즘#recentComments 참고

count = 0
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip()))

walk = [[] for _ in range(N)]

for _ in range(N-1) :
    u, v = map(int, sys.stdin.readline().split())
    walk[u-1].append(v-1)
    walk[v-1].append(u-1)
    # 연결된 정점(a, b)이 모두 실내이면
    # a -> b or b -> a 2가지 경로가 만들어진다.
    if A[u-1] == 1 and A[v-1] == 1 :
        count += 2

def dfs(v) : # v : 시작 정점
    cnt = 0
    visited[v] = 1
    stack = []
    stack.extend(walk[v])
    while stack :
        cur = stack.pop()
        if A[cur] == 1 : # 현재 노드가 실내라면 
            cnt += 1
        # 실외 노드이고 방문한 적이 없으면 계속해서 탐색
        elif visited[cur] == 0 and A[cur] == 0 :
            visited[cur] = 1
            stack.extend(walk[cur])
    return cnt

visited = [0] * N
for i in range(N) :
    if  visited[i] == 0 and A[i] == 0 : # 실외 노드라면
        # 가능한 경우의 실외노드들의 경로에 연결되어 있는 실내 노드의 개수 c
        c = dfs(i)
        # 무조건 실내에서 시작하여 실내로 끝나야 하므로
        # 현재 연결된 실내 노드 2개를 선택할 수 있는 경우의 수 만큼 경로 생성 가능
        count += c*(c-1)

print(count)
###################73점##################################################
# import sys

# N = int(sys.stdin.readline())
# # 1 = 실내, 0 = 실외
# A = sys.stdin.readline()
# count = 0

# walk = [[] for _ in range(N)]
# for _ in range(N-1) :
#     u, v = map(int, sys.stdin.readline().split())
#     walk[u-1].append(v-1)
#     walk[v-1].append(u-1)

# def dfs(start) :
#     global count
#     visited = [0] * N
    
#     visited[start] = 1
#     stack = []
#     stack.extend(walk[start])
    
#     while stack :
#         cur = stack.pop()
#         if visited[cur] == 0 :
#             visited[cur] = 1
#             if A[cur] == "0" : # 실외일 경우만  후에 더 탐색학 노드 추가
#                 stack.extend(walk[cur])
#             else : # 실내일 경우 하나의 산책로 완성
#                 count += 1

# for i in range(N) :
#     if A[i] == "1" :
#         dfs(i)
# print(count)