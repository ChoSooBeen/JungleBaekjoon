import sys

N, M = map(int, sys.stdin.readline().split())

S = {} # 문자열의 집합 -> 딕셔너리로 저장
for _ in range(N) :
    S[sys.stdin.readline().strip()] = 1

count = 0
for _ in range(M) : 
    t = sys.stdin.readline().strip()
    if t in S : #집합에 포함되어 있는지 확인
        count += 1

print(count)