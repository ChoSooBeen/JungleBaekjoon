import sys

N = int(sys.stdin.readline())

dance = {'ChongChong' : 1}
for _ in range(N) :
    a, b = sys.stdin.readline().split()
    # 두 사람 중 한 사람만 춤을 추고 있는 경우를 나눠 dance 목록에 저장
    if a in dance and b not in dance:
        dance[b] = 1
    elif a not in dance and b in dance :
        dance[a] = 1

print(len(dance))