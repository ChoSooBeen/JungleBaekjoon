x, y, w, h = map(int, input().split())

w = w - x
h = h - y

min = x

if min > y :
    min = y
if min > w :
    min = w
if min >h :
    min = h

print(min)