import sys
from itertools import permutations

# 입력받기
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

#순열 생성 -> 배열들의 원소들이 정렬되는 모든 경우를 구한다.
# https://cijbest.tistory.com/12 참고
nums_list = list(permutations(nums, N))

# 재귀적으로 순열 생성하기
# https://velog.io/@yeseolee/python으로-순열과-조합-직접-구현하기 참고
# def permutation(arr, r):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     def generate(chosen, used):
#         if len(chosen) == r:
#             print(chosen)
#             return
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#     generate([], used)

result = 0

for li in nums_list:
   sum = 0
   for j in range(N-1):
      sum += abs(li[j]-li[j+1])
   result = max(result, sum)

print(result)
