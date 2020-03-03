# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:21:38 2020

@author: Seokwoojoon
"""

import sys
N = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) +[1] for _ in range(N)]
m.append([1]*(N+1))
def dfs(y,x,d):
    global cnt 
    
    if y ==N-1 and x ==N-1:
        cnt +=1 
        return cnt
    #print(y,x)
    # 가로로 이동 
    if d != 2:
        if m[y][x+1] != 1:
            dfs(y,x+1,0)
    # 대각선 
    
    if m[y+1][x] ==0 and m[y][x+1] ==0 and m[y+1][x+1] ==0:
        dfs(y+1,x+1,1)
    #세로 
    if d!=0:
        if m[y+1][x] != 1:
            dfs(y+1,x,2)
    return cnt


if m[N-1][N-1] == 1:
    print(0)
else:
    cnt = 0 
    print(dfs(0,1,0))
    
