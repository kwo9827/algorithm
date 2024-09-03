T = int(input())

for tc in range(1,T+1):
    N= int(input())
    lst = list(map(int,input().split()))

    max_val = -99999999

    for i in range(N-1):
        sum_val = 0
        for j in range(i,i+2):
            sum_val += lst[j]

        if sum_val > max_val:
            max_val = sum_val
    print(f'#{tc} {max_val}')