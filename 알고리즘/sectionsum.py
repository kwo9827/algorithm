T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    lst = list(map(int,input().split()))

    max_sum = -99999999
    min_sum = 999999999

    for i in range(N-M+1):
        sum_1 = 0
        for j in range(i,i+M):
            sum_1 += lst[j]
        if sum_1 < min_sum:
            min_sum = sum_1
        if sum_1 > max_sum:
            max_sum = sum_1
    
    print(f'#{tc} {max_sum - min_sum}')