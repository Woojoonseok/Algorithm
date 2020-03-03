import sys

N = int(sys.stdin.readline())
m = [[0]* (N+1)] + [ [0] + list(map(int, sys.stdin.readline().split())) for i in range(N) ]

min_value = float('inf')
for d1 in range(1,N):
    for d2 in range(1,N):
        for x in range(d1 +1 , N-d2+1):
            for y in range(1, N - (d1+d2)+1):
                if d1 + d2  > N-1:
                    continue
                blank = [[0]* (N+1) for _ in range(N+1)]
                blank[y][x] = 9

                # 1 구역 
                sum_1 = 0
                for i in range(1,y+d1):
                    for j in range(1, x+1):
                        blank[i][j]=1
                        sum_1 += m[i][j]
                t = -1 
                for i in range(y,y+d1):
                    t += 1
                    for j in range(x-t,x+1):
                        blank[i][j]= 5
                        sum_1 -= m[i][j]
                
                # 2 구역 
                sum_2 = 0
                for i in range(1,y+d2+1):
                    for j in range(x+1, N+1):
                        blank[i][j]=2
                        sum_2 += m[i][j]
                t = 0
                for i in range(y,y+d2+1):
                    t += 1
                    for j in range(x+1,x+t):
                        sum_2 -= m[i][j]
                        blank[i][j]= 6
                
                # 3 구역 
                sum_3 = 0
                for i in range(y+d1, N+1):
                    for j in range(1, x-d1+d2):
                        blank[i][j]=3
                        sum_3 += m[i][j]
                t = -1
                for i in range(y+d1,  y+d1+d2+1):
                    t += 1
                    for j in range(x-d1+t, x-d1+d2):
                        blank[i][j]= 7
                        sum_3 -= m[i][j]
                        
                # 4 구역
                sum_4 = 0
                for i in range(y+d2+1, N+1):
                    for j in range(x-d1+d2, N+1):
                        blank[i][j]=4
                        sum_4 += m[i][j]
                t = -1
                for i in range(y+d2+1,  y+d1+d2+1):
                    t += 1
                    for j in range(x+d2-d1, x + d2 - t):
                        blank[i][j]= 8
                        sum_4 -= m[i][j]
                sum_5 = sum(sum(m,[])) - (sum_1 + sum_2 + sum_3 + sum_4)
                total_list = [sum_1, sum_2, sum_3, sum_4, sum_5]
                
                if min_value > max(total_list) - min(total_list):
                    min_value = max(total_list) - min(total_list)
                    
print(min_value)
                    
