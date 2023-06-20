import sys

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
result = []

def dfs(depth, idx) :
    if depth == M :
        print(*result)
        return
    for i in range(idx+1, N) :
        result.append(nums[i])
        dfs(depth+1, i)
        result.pop()
    
for i in range(N) :
    result.clear()
    result.append(nums[i])
    dfs(1, i)