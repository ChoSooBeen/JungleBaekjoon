import sys

N = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = float('inf')
# 0으로 초기화 / INF로 초기화하면 시간초과 발생
dp = [[0] * (1 << N) for _ in range(N)]

# current : 현재 도시 / visited : 방문 여부 저장 정수
def dfs(current, visited) :
    # 모든 도시를 돌았다면 -> visited = 2^N-1일 경우
    if visited == (1 << N)-1 :
        # 마지막 도시인 현재 도시에서 시작도시로 가는 길이 존재하면
        if city[current][0] :
            # 현재 도시에서 시작 도시로 가는 비용 반환
            return city[current][0]
        else :
            return INF
    
    # 만약 현재 도시에서 다음에 갈 도시에 대한 비용을 이미 계산했을 경우
    if dp[current][visited] :
        return dp[current][visited]
    
    dp[current][visited] = INF
    for i in range(1, N) :
        # 길이 존재하고 현재 방문하지 않았으면 -> 방문 여부 확인 & and 연산자 사용
        if city[current][i] != 0 and visited & (1 << i) == 0 :
            # 방문 체크 -> | or 연산자 사용
            dp[current][visited] = min(dp[current][visited], dfs(i, visited | (1 << i)) + city[current][i])
    return dp[current][visited]

print(dfs(0, 1))