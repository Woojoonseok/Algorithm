# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:52:05 2020

@author: Seokwoojoon
"""

import sys
sys.stdin = open('연산자끼워넣기.txt','r')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_val = 0
min_val = float('inf')
# DFS
def dfs(cnt,result):
    global min_val, max_val
    if cnt == len(A)-1:
        if result > max_val:
            max_val = result
        if result < min_val:
            min_val = result
        return 
    for i in range(4):
        if op[i]:
            op[i] -=1
            if i ==0:
                dfs(cnt+1, result + A[cnt+1])
            elif i ==1:
                dfs(cnt+1, result - A[cnt+1])
            elif i ==2:
                dfs(cnt+1, result * A[cnt+1])
            elif i ==3:
                if result< 0:
                    dfs(cnt+1, (-result)//A[cnt+1])
                else:
                    dfs(cnt+1, result//A[cnt+1])
            op[i] += 1 

dfs(0,A[0])
print(max_val, min_val)