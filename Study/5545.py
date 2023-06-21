import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
D = [int(sys.stdin.readline()) for _ in range(N)]
D.sort(reverse=True)

cost = A
calorie = C
best = calorie // cost

for i in range(N) :
    cost += B
    calorie += D[i]
    t = calorie // cost
    best = max(best, t)
print(best)