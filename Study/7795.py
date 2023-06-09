import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    
    A.sort()
    B.sort()
    
    count = 0
    idx = 0
    for num in A :
        # num보다 작은 B의 개수만큼 더해준다.
        while idx < M and B[idx] < num :
            idx += 1
        count += idx
    print(count)