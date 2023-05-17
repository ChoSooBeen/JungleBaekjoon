import sys
from itertools import combinations

N, M, K = map(int, sys.stdin.readline().split())

jimin = list(combinations(range(N), M)) # 지민이가 뽑을 수들의 조합
result = list(combinations(range(N), M)) # 당첨 결과들의 조합

luck = 0 # 당첨된 횟수 저장
for jm in jimin :
    for re in result :
        count = 0 # 현재 지민이와 결과가 같은 수의 개수
        for i in range(M) :
            for j in range(M) :
                if jm[i] == re[j] :
                    count += 1
        if count >= K : # 적어도 K개이므로 그 이상일 경우 당첨!
            luck += 1

print(luck/(len(jimin)**2))        