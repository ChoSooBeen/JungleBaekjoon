import sys

N, M = map(int, sys.stdin.readline().split())

words = {} # key = 영어단어 / value = 영어단어 입력 횟수
for _ in range(N) :
    w = sys.stdin.readline().strip()
    if len(w) >= M :
        if w in words :
            words[w] += 1
        else :
            words[w] = 1

# 단어를 사전 순으로 정렬
words = dict(sorted(words.items()))
# 단어를 입력 횟수가 많은 순으로 정렬하되 같으면 길이가 긴 것부터 정렬
words = dict(sorted(words.items(), key=lambda x:(x[1], len(x[0])), reverse=True))

for w  in words.keys() :
    print(w)