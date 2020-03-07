# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:01:42 2020

@author: Seokwoojoon
"""

import sys
import copy
from itertools import combinations, permutations
sys.stdin = open('bridge.txt.', 'r')

N,M = list(map(int,sys.stdin.readline().split()))
m = [list(map(int,sys.stdin.readline().split() )) for _ in range(N)]

def make_bridge(y,x,d,a,b,sea):
    global distance
    ny = y + dy[d]
    nx = x + dx[d]
    if ny <0 or ny >=N or nx <0 or nx >=M:
        return
    if m[ny][nx] == 0:
        make_bridge(ny,nx,d,a,b,sea+1)
    if m[ny][nx] == b:
        if sea >= 2:
            if distance[a][b] > sea:
                distance[a][b] = sea
                distance[b][a] = sea

def check_island(a,b):
    for y in range(N):
        for x in range(M):
            if m[y][x] == a:
                stack = []
                stack.append([y,x])
                while stack:
                    cur = stack.pop()
                    y = cur[0]; x = cur[1]

                    for d in range(4):
                        ny = y + dy[d] 
                        nx = x + dx[d]
                        if ny <0 or ny >=N or nx <0 or nx >=M:
                            continue
                        if m[ny][nx] == 0:
                            make_bridge(y,x,d,a,b,0)
            
# 섬 찾기 
def dfs(y,x, cnt):
    stack =[]
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1
    stack.append([y,x])
    m[y][x] = cnt 
    while stack:
        cur = stack.pop()
        y = cur[0]; x = cur[1]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny <0 or ny >=N or nx <0 or nx >=M or m[ny][nx] ==0:
                continue
            if visited[ny][nx] == 0:
                stack.append([ny,nx])
                visited[ny][nx] = 1
                m[ny][nx] = cnt 

def check_state(select): 
    weight =0 
    connect = [[0]*cnt for _ in range(cnt)]
    for i in range(len(bridge)):
        if select[i] == True:
            y = bridge[i][0]
            x = bridge[i][1]
            weight += bridge[i][2]
            connect[y][x] = True
            connect[x][y] = True
    q = []
    q.append(1)
    islandcnt = 1
    visited = [0] * cnt 
    visited[1] = 1 
    flag = False
    while q:
        cur = q.pop()
        if islandcnt == cnt-1:
            flag = True
            break
        for i in range(1, cnt):
            if cur ==i:
                continue
            if connect[cur][i] == True and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                islandcnt += 1 
    return [flag, weight] 
def find_combination(idx,count):
    global ans 
    if count>=1:
        flag, weight = check_state(select)
        if flag:
            ans  = min(weight, ans)
    for i in range(idx, len(bridge)):
        if select[i] == True:
            continue
        select[i] = True
        find_combination(i,count+1)
        select[i] = False
        
#=============================================================================
for i in range(N):
    for j in range(M):
        m[i][j] *= 9
dy = [0,0,1,-1]
dx = [1,-1,0,0]
cnt =0
# 각 섬에 labeling 
for y in range(N):
    for x in range(M):
        if m[y][x] ==9:
            cnt +=1 
            dfs(y,x,cnt)
cnt +=1 
distance = [[float('inf')]* (cnt) for _ in range(cnt)]
# 각 섬을 연결 + 거리 계산 
for j in combinations(list(range(1,cnt)),2):
    if len(j) ==2:
        check_island(j[0],j[1])        
bridge = {}
count =0 
for i in range(len(distance)):   
    for j in range(i, len(distance[i])):
        if distance[i][j] ==float('inf'):
            continue
        bridge[count] = [i,j, distance[i][j]]
        count += 1
ans =float('inf') 
select = [False]*(cnt)
find_combination(0,0)
if ans == float('inf'):
    print(-1)
else:
    print(ans)

        
        
            
            
        