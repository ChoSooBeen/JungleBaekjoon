import sys

start, end = map(int, sys.stdin.readline().split())
e = int(end ** (1/2))+1
arr = [True] * e

def eratos(n) :
    for i in range(2, n) :
        if arr[i] == False :
            continue
        idx = 2
        while i*idx < n :
            arr[i*idx] = False
            idx += 1

count = 0
eratos(e)
for i in range(2, e) :
    n = 2
    if arr[i] :
        tmp = int(i**n)
        while tmp <= end :
            if tmp >= start :
                count += 1
            n += 1
            tmp = int(i**n)
print(count)