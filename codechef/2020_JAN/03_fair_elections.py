"""
Problem Code - FAIRELCT

Fair Elections
"""

def solution(A, B, N, M):
    A.sort()
    B.sort(reverse=True)

    vote_diff = sum(A) - sum(B)

    i = 0
    while vote_diff <= 0 and i < min(N, M) and B[i] > A[i]:
        vote_diff += 2 * (B[i] - A[i])
        i += 1

    if vote_diff > 0:
        return i
    return -1

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(A, B, N, M))
