import sys

n = int(sys.stdin.readline())
alphabet = {}
words = []
for _ in range(n) :
    words.append(sys.stdin.readline().strip())

# https://www.acmicpc.net/board/view/85400 가중치 저장 방법
for word in words :
    for i in range(len(word)) :
        if word[i] not in alphabet :
            alphabet[word[i]] = 10 ** (len(word)-i-1)
        else :
            alphabet[word[i]] += 10 ** (len(word)-i-1)

tmp = sorted(alphabet.items(), key=lambda x: -x[1])
for i in range(len(alphabet)) :
    alphabet[tmp[i][0]] = 9 - i

result = 0
for word in words :
    for i in range(len(word)) :
        result += alphabet[word[i]] * (10 ** (len(word)-i-1))
print(result)