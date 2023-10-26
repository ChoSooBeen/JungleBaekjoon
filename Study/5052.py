import sys

input = sys.stdin.readline

t = int(input())
while t > 0 :
    t -= 1
    n = int(input())
    nums = [input().strip() for _ in range(n)]
    nums.sort()
    
    flag = True
    for i in range(n-1) :
        if nums[i] == nums[i+1][:len(nums[i])] :
            print("NO")
            flag = False
            break
    if flag :
        print("YES")