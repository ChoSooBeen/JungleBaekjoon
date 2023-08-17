import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
findNums = list(map(int, sys.stdin.readline().split()))

nums.sort()

def isExist(n) :
    start = 0
    end = N-1
    while start <= end :
        mid = (start + end)//2
        if n < nums[mid] :
            end = mid - 1
        elif n > nums[mid] :
            start = mid + 1
        else :
            return True
    return False

result = []
for num in findNums :
    if isExist(num) :
        result.append(1)
    else :
        result.append(0)
print(*result)