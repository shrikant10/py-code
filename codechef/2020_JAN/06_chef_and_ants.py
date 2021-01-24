"""
Problem Code - ANTSCHEF

Chef and Ants Problem
"""
from sys import stdin
input = stdin.readline

def solution(n, x):
    collisions = 0
    all = set()
    final = set()
    for i in range(n):
        q = 0
        s = set()
        for j in range(1, x[i][0]+1):
            if x[i][j] < 0:
                q += 1
            s.add(abs(x[i][j]))
        collisions += (len(x[i]) - 1 - q) * q
        final = final.union(all.intersection(s))
        all = all.union(s)
    collisions += len(final)
    return collisions


T = int(input())

for _ in range(T):
    N = int(input())
    X = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, X))
