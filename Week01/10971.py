import sys

N = int(sys.stdin.readline())
city = []
# 방문 여부 배열
visited = [False] * N

for i in range(N) :
    city.append(list(map(int, sys.stdin.readline().split())))

# 도시 순회 함수
# https://velog.io/@y7y1h13/알고리즘백준-10971번-외판원-순회-2python 참고

'''
start : 시작 도시
current : 현재 탐색하고 있는 도시
value : 현재까지 순회한 비용
count : 현재까지 탐색한 도시 수
'''
def dfs(start, current, value, count) :
    global result
    # 현재 도시가 마지막 도시라면
    if count == N :
        # 시작한 도시로 돌아간다.
        if city[current][start] :
            value += city[current][start]
            # 이미 저장된 탐색값보다 작을경우
            if result > value :
                result = value
        return
    # 이미 저장된 탐색값 보다 클 경우
    if value > result :
        return
    
    # 도시 수만큼 반복
    for i in range(N) :
        # 아직 탐색할 수 있는 도시가 남아있다면
        # 즉, 방문한 적이 없고 도시 비용이 0이 아닌 경우
        if not visited[i] and city[current][i] :
            visited[i] = True
            dfs(start, i, value + city[current][i], count + 1)
            visited[i] = False

result = sys.maxsize
# 도시마다 출발점 지정
for i in range(N) :
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(result)