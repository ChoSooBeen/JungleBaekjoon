import sys

def check(num) :
    hundred = num // 100
    ten = num % 100 // 10
    one = num % 100 % 10
    
    if hundred - ten == ten - one :
        return 1
    return 0

num = int(sys.stdin.readline())

if num < 100 :
    print(num)
else:
    result = 99
    for i in range(100, num+1):
        result += check(i)
    print(result)
