import sys

input = sys.stdin.readline
n, m = map(int, input().split())

truth = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]

for _ in range(m) :
    for p in party :
        if p & truth :
            truth = truth.union(p)

count = 0
for p in party :
    if not (truth & p) :
        count += 1
print(count)