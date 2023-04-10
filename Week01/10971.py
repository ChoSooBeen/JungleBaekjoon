import sys

N = int(sys.stdin.readline())
city = []
visited = [False] * N

for i in range(N) :
    city.append(list(map(int, sys.stdin.readline().split())))

# 도시 순회 함수
# https://velog.io/@y7y1h13/알고리즘백준-10971번-외판원-순회-2python 참고
def dfs(start, current, value, count) :
    global result
    if count == N :
        # 현재 도시가 마지막으로 시작한 도시로 돌아간다.
        if city[current][start] :
            value += city[current][start]
            if result > value :
                result = value
        return
    if value > result :
        return
    
    # 아직 탐색할 도시가 남아있으면
    for i in range(N) :
        if not visited[i] and city[current][i] :
            visited[i] = True
            dfs(start, i, value + city[current][i], count + 1)
            visited[i] = False

result = sys.maxsize
for i in range(N) :
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(result)