import sys

#벨만-포드 알고리즘 : 음의 가중치를 가진 최단 경로 구하기
def BellmanFord(start, n) :
    visited = [sys.maxsize] * (n+1)
    
    visited[start] = 0
    for i in range(1, n+1) :
        for r in roads :
            s, e, t = r
            if visited[e] > t + visited[s] :
                visited[e] = t + visited[s]
                if i == n :
                    return True
    return False

t = int(sys.stdin.readline())
for _ in range(t) :
    n, m, w = map(int, sys.stdin.readline().split())
    roads = []
    for _ in range(m) :
        s, e, t = map(int, sys.stdin.readline().split())
        roads.append((s, e, t))
        roads.append((e, s, t))
    for _ in range(w) :
        s, e, t = map(int, sys.stdin.readline().split())
        roads.append((s, e, -t))
        
    if BellmanFord(1, n) :
        print("YES")
    else :
        print("NO")