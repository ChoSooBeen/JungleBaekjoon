import sys
from collections import deque

testcase = int(sys.stdin.readline())
for _ in range(testcase) :
    N, M = map(int, sys.stdin.readline().split())
    priorty = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    
    for i in range(N) :
        queue.append((i, priorty[i])) # 원래 위치와 중요도를 같이 큐에 넣어준다.

    count = 0
    while queue :
        flag = True #True일 경우 출력 가능 / False일 경우 재배치
        idx ,cur = queue.popleft()
        for i in range(len(queue)):
            if cur < queue[i][1] : # 현재 우선순위보다 큰 우선순위가 존재하면
                flag = False
                queue.append((idx, cur))
                break
        if flag : # 출력가능하면
            count += 1
            if idx == M : #현재 문서가 M번에 있던 문서일 경우
                break
    print(count)