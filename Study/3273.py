import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
x = int(sys.stdin.readline())

count = 0
# 1 2 3 5 7 9 10 11 12
start = 0
end = n-1

while start < end :
    t = nums[start] + nums[end]
    if t == x :
        count += 1
        start += 1
        end -= 1
    elif t > x :
        end -= 1
    else :
        start += 1
print(count)