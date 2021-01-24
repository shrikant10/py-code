"""
Problem Code - WIPL

Watching CPL
"""

def solution(n, k, h):
    asum = sum(h)
    if n == 1 or asum < 2 * k: return -1
    h.sort(reverse=True)
    if asum == 2 * k:
        if h[0] > k: return -1
        if h[0] == k: return n
    if h[0] >= k:
        i, B = 1, 0
        while i < n and B < k:
            B += h[i]
            i += 1
        if B >= k: return i
        return -1
    mat = [[False] * (asum + 1)]
    mat[0][0] = True

    def find_min_diff(n, total, is_new, old_total):
        for i in range(1, n + 1):
            if not is_new and i == n:
                old_total = 1
            for j in range(old_total, total // 2 + 1):
                mat[i][j] = mat[i - 1][j]
                if h[i - 1] <= j:
                    mat[i][j] = mat[i][j] or mat[i - 1][j - h[i - 1]]
        for j in range(total // 2, k - 1, -1):
            if mat[n][j]: return True
        return False

    total = 0
    new = True
    for i in range(n):
        total += h[i]
        mat.append([False] * (asum + 1))
        mat[i + 1][0] = True
        if total >= 2 * k:
            old_total = 1 if new else (total - h[i]) // 2
            if find_min_diff(i + 1, total, new, old_total):
                return i + 1
            new = False
    return -1


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    print(solution(N, K, H))
