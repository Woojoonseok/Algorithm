# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:58:20 2020

@author: Seokwoojoon
"""

import sys
import copy
sys.stdin = open('sample.txt','r')


m = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
paper_list = [0,5,5,5,5,5]
cnt = 0
result = float('inf')
def dfs(y,x):
    global cnt, result
    N = 10
    if x == N:
        dfs(y+1, 0)
        return 
    if y ==N:
        result = min(result, cnt)
        #print(paper_list)
        return 
    if m[y][x] == 0:
        dfs(y,x+1)
        return 
    for i in range(5,0,-1):
        # 색종이 확인, 범위 확인 
        if paper_list[i] ==0 or y + i > N or x + i > N:
            continue
        # 정사각형 확인 
        flag = True
        for yy in range(i):
            for xx in range(i):
                if m[y+yy][x+xx] ==0:
                    flag = False
            if flag==False:
                break
        # 0 있으면 return 
        if flag == False:
            continue
        # 다시 덮는다. 
        for yy in range(i):
            for xx in range(i):
                m[y+yy][x+xx] = 0  
        paper_list[i] -= 1
        cnt +=1
        dfs(y, x+i)
        for yy in range(i):
            for xx in range(i):
                m[yy+y][xx+x] = 1
        paper_list[i] += 1
        cnt -= 1 

dfs(0,0)
if result == float('inf'):
    print(-1)
else:
    print(result)
    

    
