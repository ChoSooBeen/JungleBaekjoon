import sys

x = sys.stdin.readline()

if x[0] == '0' :
    if x[1] == 'x' :
        print(int(x, 16))
    else :
        print(int(x, 8))
else :
    print(int(x))