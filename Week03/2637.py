import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

basic = [[] for _ in range(N)]
inDegree = [0] * N

for _ in range(M) :
    x, y, k = map(int, sys.stdin.readline().split())
    basic[y-1].append((x-1, k))
    inDegree[x-1] += 1

def topologicalsort() :
    # component[x][y] -> x를 만드는데 필요한 y의 개수
    component = [[0] * N for _ in range(N)]
    queue = deque()
    
    for i in range(N) :
        if inDegree[i] == 0 : # 차수 0 = 기본 부품
            queue.append(i)
            # 기본 부품은 자기 자신을 1개 가지고 있으면 된다.
            component[i][i] = 1
    
    while queue :
        cur = queue.popleft()
        # cur를 이용하여 next를 만드는데 필요한 개수 = count
        for next, count in basic[cur] :
            for i in range(N) :
                # 예시) cur = 5 / next = 7 / i = 1
                # 7을 만들기 위해 필요한 5의 개수 2 = count
                # 5를 만들기 위해 필요한 1의 개수 2 = component[cur][i]
                # 7을 만들기 위해 필요한 5를 위해 필요한 1의 개수 = 2 * 2
                component[next][i] += component[cur][i] * count
            inDegree[next] -= 1
            if inDegree[next] == 0 :
                queue.append(next)
    for i in range(N) :
        # 마지막 완제품을 만들 때 필요한 부품들 = component[N-1]
        if component[N-1][i] > 0 : # 값이 0인 경우 중간 부품이다.
            print(f'{i+1} {component[N-1][i]}')

topologicalsort()