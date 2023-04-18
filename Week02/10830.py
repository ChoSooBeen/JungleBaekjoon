import sys

N, B = map(int, sys.stdin.readline().split())

p = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 두 행렬을 곱하는 함수
def mul (a, b) :
    result = [[0] * N for _ in range(N)]
    for r in range(N) :
        for c in range(N) :
            for i in range(N) :
                result[r][c] += a[r][i] * b[i][c]
            result[r][c] %= 1000
    return result

# 제곱근을 분할하는 함수
def getResult(p, b) :
    if b == 1 :
        for i in range(N) :
            for j in range(N) :
                p[i][j] %= 1000
        return p
    else :
        tmp = getResult(p, b//2)
        if b % 2 == 0 :
            return mul(tmp, tmp)
        else :
            return mul(mul(tmp, tmp), p)

ans = getResult(p, B)
for a in ans :
    # unpacking
    print(*a)