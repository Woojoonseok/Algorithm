# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:38:49 2020

@author: Seokwoojoon
"""

import sys
dy = [0,0,1,-1]
dx = [1,-1,0,0]
sys.stdin = open('sample_input.txt')
T = int(sys.stdin.readline())
for test_case in range(1,T+1):
    N = int(sys.stdin.readline())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    #print(m)
    if test_case ==2:
        break
    visited=[[0]*N for i in range(N)]
    
    for d1 in range(1,N):
        for d2 in range(1,N):
            for y in range(N):
                for x in range(1,N):
                    if y+d1+d2>=N:
                        break
                    if x - d1 >= x or x+d2 >= N:
                        break
                    
                    # 경계선 구하기 
                    visited=[[0]*N for i in range(N)]
                    visited[y][x] = 5
                    for i in range(1, d1+1):
                        visited[y+i][x-i] = 5
                    for i in range(1, d2+1):
                        visited[y+i][x+i] = 5
                    for i in range(1, d2+1):
                        visited[y+d1+i][x-d1+i] = 5
                    for i in range(1, d1+1):
                        visited[y+d2+i][x+d2-i] = 5
                    
                    # 각 선거구 표시
                    # 1, 0 에서 x+d1 까지 5가 있는지 없는지 판별 
                    # 5가 있으면 5번 선거구에 포함되어 있음
                    # 5가 없으면 5번 선거구에 포함되어 있지 않음
                    #print(d1,d2,x,y)
                    
                    # 1구역 합 구하기 
                    s1 = 0
                    for i in range(x+1):
                        for j in range(y + d1):
                            if visited[j][i] == 5:
                                break
                            visited[j][i] = 1 
                            s1 += m[j][i] 
                    
                    s2 =0
                    for i in range(x+1, N):
                        for j in range(y+d2+1):
                            if visited[j][i] == 5:
                                break
                            visited[j][i] = 2
                            s2 += m[j][i]
                    
                    s3 =0 
                    for j in range(y+d1, N):
                        for i in range(x-d1+d2):    
                            #print(j,i)
                            if visited[j][i] == 5:
                                break
                            visited[j][i] = 3
                            s3 += m[j][i]
                    s4 =0 
                    for j in range(y+d2+1, N): 
                        for i in range(x-d1+d2,N): 
                            if visited[j][i] == 5 or visited[j][i] !=0 :
                                continue
                            if i <0:
                                continue
                            print('j,i', [j,i], 'y, x',  [y, x], d2-d1 )
                            visited[j][i] = 4
                            s4 += m[j][i]
                    print('a')
                    
                    
                        
                    #         if visited[ny][nx] ==5:
                    #             flag = 1
                    #     # 5가 있을 때 (5번 선거구에 속해있음) 
                    #     if flag:
                    #         for i in range(N):
                    #             if visited[ny][i] == 5:
                    #                 break
                    #             visited[ny][i] = 1
                    #             flag =0
                    #     #5가 없을 때 (5번 선거구에 포함X)
                    #     else:
                    #         for i in range(x+d1+1):
                    #             visited[ny][i] = 1
                    # print('a')
                            
                
                

