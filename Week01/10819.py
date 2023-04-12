import sys

# 입력받기
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 최종 결과값 저장할 변수
result = 0

# 사용여부를 저장할 배열
used = [0] * N
   
# 순열 생성 함수
def generate(chosen, used):
   global result
   if len(chosen) == N:
      # 현재 리스트의 차이의 합을 저장할 변수
      sum = 0
      for i in range(N-1):
         sum += abs(chosen[i]-chosen[i+1])
      result = max(result, sum)
      return 
   
   # 순열생성
   for i in range(len(nums)):
      if not used[i]:
         chosen.append(nums[i])
         used[i] = 1
         generate(chosen, used)
         used[i] = 0
         chosen.pop()
generate([], used)
print(result)