import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1, N+1) :
    num = i
    sum = i
    while num != 0 :
        sum += num % 10
        num = num // 10
    if sum == N :
        result = i
        break
print(result)