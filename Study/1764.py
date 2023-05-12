import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N) :
    dic[sys.stdin.readline().strip()] = 1

count = 0
result = []
for _ in range(M) :
    b = sys.stdin.readline().strip()
    if b in dic :
        count += 1
        result.append(b)

print(count)
result.sort()
for i in range(count) :
    print(result[i])