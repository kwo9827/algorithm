T = int(input())

for tc in range(1,T+1):
    N= int(input())
    lst =list(map(int,input().split()))

    max_val = -999999999999
    max_idx = 0
    max_cont = 0

    for i in range(N):
        if lst[i] > max_val:
            max_val = lst[i]
            max_idx = i
        
        cont = 0
        for j in range(max_idx,N):
            
            if lst[j] < max_val:
                cont += 1
 
        if cont > max_cont:
            max_cont = cont

    print(f'#{tc} {max_cont}')