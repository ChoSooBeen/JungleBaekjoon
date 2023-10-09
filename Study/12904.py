import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

flag = False

while t :
    if t[-1] == 'A' :
        t.pop()
    elif t[-1] == 'B' :
        t.pop()
        t.reverse()
    if s == t :
        flag = True
        break
if flag :
    print(1)
else :
    print(0)