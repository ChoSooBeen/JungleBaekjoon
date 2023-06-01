import sys

n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(n+1)]

def find(x) :
    y = x
    while y != lst[y] :
        y = lst[y]
    lst[x] = y # 한번이라도 루트를 찾으면 그 루트를 저장하기!
    return y

def union(x, y) :
    x = find(x)
    y = find(y)
    
    if x != y :
        if x > y :
            lst[x] = y
        else :
            lst[y] = x

for _ in range(m) :
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0 :
        union(a, b)        
    else :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")