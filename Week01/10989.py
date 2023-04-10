import sys

n = int(sys.stdin.readline())
nums = [0] * 10001

while n > 0 :
    nums[int(sys.stdin.readline())] += 1
    n -= 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)