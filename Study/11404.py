import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distacne = [[sys.maxsize] * (n+1) for _ in range(n+1)] #distance[x][y] = z : x에서 y로 가는 비용 z이다.
for _ in range(m) :
    x, y, z = map(int, sys.stdin.readline().split())
    if distacne[x][y] > z :
        distacne[x][y] = z

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if distacne[i][j] > distacne[i][k] + distacne[k][j] :
                distacne[i][j] = distacne[i][k] + distacne[k][j]
                
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if distacne[i][j] == sys.maxsize or i == j :
            print(0, end=" ")
        else :
            print(distacne[i][j], end=" ")
    print()