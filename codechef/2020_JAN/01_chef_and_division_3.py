"""
Problem Code - DIVTHREE

Chef and Division 3
"""

T = int(input())

for _ in range(T):
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)
    days = total//K
    if days > D:
        days = D
    print(days)
