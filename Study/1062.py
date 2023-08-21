import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

# 필수 글자 : a, n, t, i, c
# 즉, 5개 미만을 가르치면 읽을 수 있는 글자가 없다.

def word2bit(word) :
    bit = 0
    for c in word :
        bit = bit | (1 << ord(c) - ord('a'))
    return bit

if K < 5 :
    print(0)
else :
    bits = list(map(word2bit, words))
    base_bit = word2bit('antic')
    
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    
    max_count = 0
    for combination in combinations(alphabet, K-5) :
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits :
            if bit & know_bit == bit :
                count += 1
        max_count = max(max_count, count)
    print(max_count)