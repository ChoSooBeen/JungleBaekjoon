import sys 

width , height = map(int, sys.stdin.readline().split())

w = [0, width]
h = [0, height]

cut = int(sys.stdin.readline())
while cut > 0 :
    flag, num = map(int, sys.stdin.readline().split())
    if flag == 0 :
        h.append(num)
    else :
        w.append(num)
    cut -= 1

h.sort()
w.sort()

a, b = 0, 0
for i in range(1, len(h)) :
    tmp = h[i] - h[i-1]
    if tmp > a :
        a = tmp
for i in range(1, len(w)):
    tmp = w[i] - w[i-1]
    if tmp > b :
        b = tmp
print(a * b)