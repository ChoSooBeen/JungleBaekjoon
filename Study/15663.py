import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

result = {}
visited = [False] * n

def dfs(count, res) :
    if count == m :
        if res not in result :
            result[res] = 1
            return
        return
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            dfs(count+1, res + str(nums[i]) + ' ')
            visited[i] = False
dfs(0, '')
for r in result :
    print(r)