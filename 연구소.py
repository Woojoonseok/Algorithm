# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:31:45 2020

@author: Seokwoojoon
"""

import sys
from itertools import combinations
import copy
from collections import deque
sys.stdin = open('연구소.txt','r')
N, M = list(map(int, sys.stdin.readline().split()))
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [0,0,-1,1]
dx = [1,-1,0,0]
# 벽세우기
# NxM 중에 3 개 선택 , 만약 바이러스거나 이미 벽이 있으면 넘어감 (경우의 수 너무 많음)
# 벽, 바이러스를 따로 저장. 안전한 장소 중 3개 선택 
virus=[]
blank=[]
result = 0
for y in range(N):
    for x in range(M):
        if m[y][x] == 0:
            blank.append([y,x])
        if m[y][x] == 2:
            virus.append([y,x])

def bfs():
    global result
    visited = [[0]*M for _ in range(N)]
    q = deque([])
    for y in range(N):
        for x in range(M):
            if m2[y][x] == 2:
                q.append([y,x])
                visited[y][x] = 1 
    while q:
        cur = q.popleft()
        y,x = cur[0], cur[1]
        m2[y][x] = 2
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >=N or nx <0 or nx >=M:
                continue
            if visited[ny][nx]==0 and m2[ny][nx] ==0:
                visited[ny][nx] = 1 
                q.append([ny,nx])
    cnt =0 
    for y in range(N):
        for x in range(M):
            if m2[y][x] ==0:
                cnt +=1 
    if cnt > result:
        result = cnt 
                
arry = [0]* len(blank)
vi = [0]*len(blank)
def dfs(cnt):
    global m2
    if cnt==3:
        #print(arry[:M])
        m2 = copy.deepcopy(m)
        b1,b2,b3 = blank[arry[0]],blank[arry[1]],blank[arry[2]]
        m2[b1[0]][b1[1]] = 1 
        m2[b2[0]][b2[1]] = 1
        m2[b3[0]][b3[1]] = 1
        bfs()
        return 0
    for i in range(cnt, len(blank)):
        if not vi[i] and arry[cnt-1] <= i :
            vi[i] = 1
            arry[cnt] = i 
            dfs(cnt+1)
            vi[i] = 0 
dfs(0)
print(result)      

#파이썬 내장함수 combination으로 N개중 M개 선택
for i in combinations(blank,3):
    m2 = copy.deepcopy(m)
    b1,b2,b3 = i[0],i[1],i[2]
    m2[b1[0]][b1[1]] = 1 
    m2[b2[0]][b2[1]] = 1
    m2[b3[0]][b3[1]] = 1
    bfs()
print(result)