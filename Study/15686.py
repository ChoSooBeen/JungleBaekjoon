import sys

n, m = map(int, sys.stdin.readline().split())
house = []
chicken = []
select  = []
result = sys.maxsize

for i in range(n) :
    input = sys.stdin.readline().strip().split()
    for j in range(n) :
        if input[j] == '1' :
            house.append((i+1, j+1))
        elif input[j] == '2' :
            chicken.append((i+1, j+1))

def dfs(count, idx) :
    global result
    value = 0
    if count == m :
        for x, y in house :
            dist = sys.maxsize
            for cx, cy in select :
                dist = min(dist, abs(x-cx) + abs(y-cy))
            value += dist
        result = min(result, value)
        return
    for i in range(idx, len(chicken)) :
        select.append(chicken[i])
        dfs(count+1, i+1)
        select.pop()

dfs(0, 0)
print(result)