import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

up = [1] * n
down = [1] * n

for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            up[i] = max(up[i], up[j] + 1)
        if b[i] > b[j] :
            down[i] = max(down[i], down[j] + 1)

result = 0
for i in range(n) :
    result = max(result, up[i] + down[n-i-1])
print(result-1)