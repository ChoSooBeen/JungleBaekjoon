import sys

n = int(sys.stdin.readline())

def round(num) :
    if num - int(num) >= 0.5 :
        return int(num) + 1
    return int(num)

if n > 0 :
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    nums.sort()
    k = round(n * 0.15)
    print(round(sum(nums[k:n-k])/(n-k*2)))
else :
    print(0)