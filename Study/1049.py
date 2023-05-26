import sys

N, M = map(int, sys.stdin.readline().split())

min_six = sys.maxsize
min_one = sys.maxsize
# 가장 작은 가격 구하기
for _ in range(M) :
    six, one =  map(int, sys.stdin.readline().split())
    if min_six > six :
        min_six = six
    if min_one > one :
        min_one = one

count = N // 6 #6의 배수가 되도록하면서 적어도 N보다 큰 몫 구하기 
while 6 * count <= N :
    count += 1

a = min_six * count # 묶음으로만 구매할 경우
b = min_one * N #낱개로만 구매할 경우
c = min_six * (count-1) + min_one * (N - (count - 1) * 6) #섞어서 구매할 경우
print(min(a,b,c))