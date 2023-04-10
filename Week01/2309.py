import sys

nums = []

for i in range(9) :
    nums.append(int(sys.stdin.readline()))

nums.sort()
sum = sum(nums)

one , two = 0, 0
flag = False

for i in range(8):
    for j in range(i+1, 9):
        if sum - (nums[i]+nums[j]) == 100 :
            one = nums[i]
            two = nums[j]
            flag = True
            break
    if flag :
        break
nums.remove(one)
nums.remove(two)

for i in nums:
    print(i)