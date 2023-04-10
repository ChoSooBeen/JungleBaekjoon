import sys
import math

def isPrime(n) :
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

T = int(sys.stdin.readline())
result = ""
while T > 0 :
    num = int(sys.stdin.readline())
    a, b = num // 2, num // 2
    while a > 0 :
        if isPrime(a) and isPrime(b) :
            result += f'{a} {b}\n'
            break
        else :
            a -= 1
            b += 1
    T -= 1
print(result)