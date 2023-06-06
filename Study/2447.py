import sys

N = int(sys.stdin.readline())
graph = [[True] * N for _ in range(N)]

def star(n, x, y) :
    if n == 3 :
        graph[x+1][y+1] = False
        return
    size = n//3
    nx, ny = x + size, y + size
    for i in range(size) :
        for j in range(size) :
            graph[nx+i][ny+j] = False
    star(size, x, y)
    star(size, x+size, y)
    star(size, x+2*size, y)
    star(size, x, y+size)
    star(size, x+2*size, y+size)
    star(size, x, y+2*size)
    star(size, x+size, y+2*size)
    star(size, x+2*size, y+2*size)

star(N, 0, 0)
for i in range(N) :
    for j in range(N) :
        if graph[i][j] :
            print("*", end="")
        else :
            print(" ", end="")
    print()