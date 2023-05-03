import sys

N = int(sys.stdin.readline())

start = 1 # 현재 더한 값 중 첫번째 값
end = 1 # 현재 더한 값 중 마지막 값
count = 1 # 자기 자신 포함
sum = 1 # 총 더한 값

# 최소 2개의 연속된 자연수의 합이어야 하므로 
# start는 N의 절반보다 클 수 없다.
while start != N // 2 + 1 :
    if sum < N : # 아직 누적합이 N보다 작을 경우
        end += 1
        sum += end
    elif sum == N : # N과 같을 경우
        count += 1
        sum -= start
        start += 1
    else : # N보다 클 경우
        sum -= start
        start += 1
print(count)