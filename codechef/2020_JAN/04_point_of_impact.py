"""
Problem Code - BILLRD

Point Of Impact
"""


def solution(n, k, x, y):
    if x == y:
        return n, n
    if x > y:
        a, b = n, y + (n - x)
    else:
        a, b = x + (n - y), n
    k = k % 4

    if k == 1: return a, b
    a, b = b, a
    if k == 2: return a, b
    a, b = a - min(a, b), b - min(a, b)
    if k == 3: return a, b
    a, b = b, a
    return a, b


T = int(input())

for _ in range(T):
    N, K, X, Y = map(int, input().split())
    print(' '.join(map(str, solution(N, K, X, Y))))
