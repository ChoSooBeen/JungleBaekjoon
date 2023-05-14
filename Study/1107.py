import sys

N = int(sys.stdin.readline()) #목표 채널
M = int(sys.stdin.readline()) # 망가진 번호 수
brocken = {}
if M :
    for i in list(sys.stdin.readline().split()) :
        brocken[i] = 1

count = abs(100 - N) # + 또는 - 로만 움직였을 때 횟수

if count != 0 : # 이미 목표 채널이 아닐 경우만 반복
    for i in range(1000001) :
        num = str(i) #현재 채널 번호
        length = len(num)
        for j in range(length) :
            if num[j] in brocken : #채널번호에 망가진 번호가 존재하면 갈수 없음
                break
            elif j == length-1 :
                # 목표 번호 - 현재 번호 = + or -로 이동한 횟수
                # length = 현재 번호로 이동하기 위헤 누른 횟수
                count = min(count, abs(N-i) + length)
print(count)