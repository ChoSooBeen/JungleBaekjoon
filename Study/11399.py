import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()

result = 0
t = 0
for i in range(N) :
    t += time[i]
    result += t
print(result)