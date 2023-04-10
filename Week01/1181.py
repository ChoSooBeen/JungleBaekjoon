import sys

N = int(sys.stdin.readline())
word = []

while N > 0:
    s = sys.stdin.readline().strip()
    word.append([len(s), s])
    N -= 1

word.sort(key=lambda x: (x[0], x[1]))

print(word[0][1])

for i in range(1, len(word)):   
    if word[i-1][1] != word[i][1]:
        print(word[i][1])