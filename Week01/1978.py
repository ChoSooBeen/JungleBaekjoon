import sys 
import math

def isPrime(n) :
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = 0
for n in nums :
    if isPrime(n) :
        count += 1

print(count)