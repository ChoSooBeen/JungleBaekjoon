import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
dic = {}

def dfs(count, result, idx) :
    if count == m :
        dic[result] = 1
        return
    for i in range(idx, n) :
        dfs(count+1, result+str(nums[i])+" ", i)

dfs(0, '', 0)
for k in dic :
    print(k)