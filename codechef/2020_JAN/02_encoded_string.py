"""
Problem Code - DECODEIT

Encoded String
"""

bin_to_dec = lambda s: sum([int(s[i])*(2**(3-i)) for i in range(4)])

T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    ans = ''
    for i in range(0, N, 4):
        curr = bin_to_dec(S[i:i+4])
        ans += chr(ord('a') + curr)
    print(ans)
