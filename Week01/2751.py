import sys

n = int(sys.stdin.readline())
nums = []

while n > 0 :
    nums.append(int(sys.stdin.readline()))
    n -= 1

nums.sort()

for i in nums:
    print(i)