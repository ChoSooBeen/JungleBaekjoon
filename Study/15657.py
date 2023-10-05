import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))

def dfs(count, result, idx) :
    if count == m :
        print(result)
        return
    for i in range(idx, n) :
        dfs(count+1, result+str(nums[i])+" ", i)

dfs(0, '', 0)