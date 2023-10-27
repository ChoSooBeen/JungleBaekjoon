import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

if nums[0] > 1 :
    print(1)
else : 
    t = nums[0]
    for i in range(1, n) :
        if t + 1 >= nums[i] :
            t += nums[i]
        else :
            break
    print(t + 1)