import sys

N = int(sys.stdin.readline())
result = []

idx = 2
while N // idx != 0 :
    if N % idx == 0 :
        result.append(idx)
        N //= idx
    else :
        idx += 1
for i in result :
    print(i)