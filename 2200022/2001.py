# 2001 파리 퇴치

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(N)]
    a = []
    for i in range(N-M+1):
        for j in range(N-M+1):