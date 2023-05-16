import sys

N, kim, im = map(int, sys.stdin.readline().split())

count = 0
flag = True
if N % 2 == 0 : #참가자가 홀수일 경우
    N += 1
    
while N > 0 :
    # 다음 경기에서의 번호 구하기
    if kim % 2 == 0 and im % 2 == 0:
        kim //= 2
        im //= 2
    elif kim % 2 != 0 and im % 2 == 0:
        kim = (kim+1) //2
        im //= 2
    elif kim % 2 == 0 and im % 2 != 0:
        kim //= 2
        im = (im+1) //2
    else :
        kim = (kim+1) //2
        im = (im+1) //2
    count += 1
    # 둘의 번호가 같다면 대결한다는 의미
    if kim == im :
        flag = False
        break
    N //= 2

if flag :
    print(-1)
else :
    print(count)