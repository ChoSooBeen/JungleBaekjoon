import sys
from itertools import permutations

# 입력받기
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

#순열 생성 -> 배열들의 원소들이 정렬되는 모든 경우를 구한다.
# https://cijbest.tistory.com/12 참고
nums_list = list(permutations(nums, N))

result = 0

for li in nums_list:
   sum = 0
   for j in range(N-1):
      sum += abs(li[j]-li[j+1])
   result = max(result, sum)

print(result)
