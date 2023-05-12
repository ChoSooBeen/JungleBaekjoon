import sys

N, M = map(int, sys.stdin.readline().split())
dic = {} #듣도 못한 사람
for _ in range(N) :
    dic[sys.stdin.readline().strip()] = 1

count = 0
result = []
for _ in range(M) :
    #보도 못한 사람
    b = sys.stdin.readline().strip()
    if b in dic.keys() :
        count += 1
        result.append(b)

print(count)
result.sort()
for i in range(count) :
    print(result[i])