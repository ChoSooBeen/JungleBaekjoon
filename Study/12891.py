import sys

s, p = map(int, sys.stdin.readline().split())
dna = list(sys.stdin.readline().strip())
# A, C, G, T
esssential = list(map(int, sys.stdin.readline().split()))

def remove(st) :
    global a, c, g, t
    if dna[st] == 'A' :
        a -= 1
    elif dna[st] == 'C' :
        c -= 1
    elif dna[st] == 'G' :
        g -= 1
    elif dna[st] == 'T' :
        t -= 1
    return 0

def add(e) :
    global a, c, g, t
    if dna[e] == 'A' :
        a += 1
    elif dna[e] == 'C' :
        c += 1
    elif dna[e] == 'G' :
        g += 1
    elif dna[e] == 'T' :
        t += 1
    return 0

start = 0
end = p-1
count = 0
# 현재 부분 문자열
current = dna[0:p]
# 각각의 원소 포함 개수
a = current.count("A")
c = current.count("C")
g = current.count("G")
t = current.count("T")

while end < s :
    # 만약에 모든 원소들의 조건을 충족했다면
    if a >= esssential[0] and c >= esssential[1] and g >= esssential[2] and t >= esssential[3] :
        count += 1
    remove(start)
    start += 1
    end += 1
    if end == s :
        break
    add(end)
    
print(count)