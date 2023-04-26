# 위상 정렬 - 임계 경로
# https://www.acmicpc.net/problem/1948

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

road = [[] for _ in range(n)]
for _ in range(m) :
    s, e, t = map(int, sys.stdin.readline().split())
    road[s-1].append((e-1, t))

start, end = map(int, sys.stdin.readline().split())
