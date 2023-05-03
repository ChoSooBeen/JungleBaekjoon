import sys
from collections import deque

s, p = map(int, sys.stdin.readline().split())
dna = list(sys.stdin.readline().strip())
# A, C, G, T
esssential = list(map(int, sys.stdin.readline().split()))

start = 0
end = p-1
count = 0
# 현재 부분 문자열
current = deque(dna[0:p])
# 각각의 원소 포함 개수
a = current.count("A")
c = current.count("C")
g = current.count("G")
t = current.count("T")

while end < s :
    # 만약에 모든 원소들의 조건을 충족했다면
    if a >= esssential[0] and c >= esssential[1] and g >= esssential[2] and t >= esssential[3] :
        count += 1
    # 가장 첫번째 값 제거
    current.popleft()
    # 각각의 원소 개수 중 일치하는 것 빼기
    if dna[start] == 'A' :
        a -= 1
    elif dna[start] == 'C' :
        c -= 1
    elif dna[start] == 'G' :
        g -= 1
    elif dna[start] == 'T' :
        t -= 1
    
    start += 1
    end += 1
    # end가 끝에 도달했으므로
    if end == s :
        break
    # 맨뒤에 문자 하나 추가
    current.append(dna[end])
    # 각각의 원소 개수 중 일치하는 것 추가
    if dna[end] == 'A' :
        a += 1
    elif dna[end] == 'C' :
        c += 1
    elif dna[end] == 'G' :
        g += 1
    elif dna[end] == 'T' :
        t += 1
print(count)