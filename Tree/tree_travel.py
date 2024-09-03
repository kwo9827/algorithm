import sys
sys.stdin = open('input1.txt')

def dfs(v):
    global cont, N
    if v > N:
        return

    dfs(v*2)
    tree[v] = cont
    cont+=1
    dfs(v*2+1)

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    cont = 1
    tree = [0] * (N+1)

    dfs(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')