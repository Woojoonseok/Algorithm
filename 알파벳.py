# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:25:17 2020

@author: Seokwoojoon
"""

import sys
#sys.stdin = open('sample.txt','r')

R, C = list(map(int, sys.stdin.readline().split()))
#R, C = 2,4
m = [sys.stdin.readline().split() for _ in range(R)] 

m2 = [ [0]*C for _ in range(R)]
alphabet = [False]*26  
for idx, i in enumerate(m):
    for idx2, j in enumerate(i[0]):
        m2[idx][idx2] = j

#visited = [ [False]*C for _ in range(R)]
dy= [0,0,1,-1]
dx =[1,-1,0,0]
result = 0 
def dfs(y,x, dist):
    global result
    result = max(result, dist)
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny <0 or ny >=R or nx <0 or nx >=C:
            continue
        K = ord(m2[ny][nx])-ord('A')
        if alphabet[K] == True:
            continue
        #print(ny, nx, K)
        alphabet[K] = True 
        dfs(ny, nx, dist+1)
        alphabet[K] = False
alphabet[ord(m2[0][0])-ord('A')] = True
dfs(0,0,1)
print(result)
