import sys

n = int(sys.stdin.readline())
nums = []

while n > 0 :
    nums.append(int(sys.stdin.readline()))
    n -= 1

n = len(nums)
k = 0

#버블 정렬
while k < n-1:
    last = n-1
    for i in range(n-1, k, -1) :
        if nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            last = i
    k = last

for i in nums:
    print(i)