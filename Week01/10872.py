import sys

def fac(num) :
    if num < 2 :
        return 1
    else :
        return num * fac(num -1)

N = int(sys.stdin.readline())
print(fac(N))