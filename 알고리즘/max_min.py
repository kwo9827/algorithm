T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    max_idx = lst[0]
    min_idx = lst[0]

    for i in range(N):
        if lst[i] > max_idx:
            max_idx = lst[i]
        if lst[i] < min_idx:
            min_idx = lst[i] 

    print(f'#{tc} {max_idx - min_idx}')