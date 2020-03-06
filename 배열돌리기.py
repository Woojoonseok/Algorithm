# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:54:49 2020

@author: Seokwoojoon
"""

import sys
import copy
from itertools import combinations, permutations
sys.stdin = open('array.txt.', 'r')

N,M,K = list(map(int,sys.stdin.readline().split()))
m = [list(map(int,sys.stdin.readline().split() )) for _ in range(N)]
ins = [list(map(int,sys.stdin.readline().split() )) for _ in range(K)]

ans = float('inf')
def cal(m):
    min_val = float('inf')
    for i in m:
        min_val = min(sum(i), min_val)
    return min_val
for i in permutations(list(range(K)),K):
    backup = copy.deepcopy(m)
    order=[j for j in i]
    for j in order:
        r, c,S = ins[j]
        r -=1; c-=1
        for s in range(1,S+1):
            temp = []
            for i in range(c-s, c+s+1):
                #print(r,c,i,backup[r-s][i])
                temp.append(backup[r-s][i])
            for i in range(r-s+1, r+s+1):
                #print(i, backup[i][c+s])
                temp.append(backup[i][c+s])
            for i in range(c+s-1, c-s-1,-1):
                #print(m[r+s][i])
                temp.append(backup[r+s][i])
            for i in range(r+s-1, r-s,-1):
                #print(m[i][c-s])
                temp.append(backup[i][c-s])
            #print('d')
            t = temp.pop(-1)
            temp.insert(0,t)
            idx =0 
            for i in range(c-s, c+s+1):
                backup[r-s][i] = temp[idx]
                idx += 1 
            for i in range(r-s+1, r+s+1):
                backup[i][c+s] = temp[idx]
                idx +=1 
            for i in range(c+s-1, c-s-1,-1):
                backup[r+s][i] =temp[idx]
                idx +=1 
            for i in range(r+s-1, r-s,-1):
                backup[i][c-s]=temp[idx]
                idx += 1

    temp_ans = cal(backup)
    ans = min(temp_ans, ans)
print(ans)