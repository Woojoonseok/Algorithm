# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:57:04 2020

@author: Seokwoojoon
"""

import copy
import sys
with open("미로탐색.txt",'r') as f:
    N,M = list(map(int, f.readline().split()))
    m = [[0]*M for _ in range(N)]
    for i in range(N):
        temp = f.readline()
        for j in range(M):
            m[i][j] = int(temp[j])
        
dy = [0,0,-1,1]
dx = [1,-1,0,0]

def bfs(y,x):
    global ans,visited
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1 
    q = []
    cnt = 1
    q.append([y,x,cnt])
    ans = float('inf')
    while q:
        y,x,cnt = q.pop(0)
        if y==N-1 and x ==M-1:
            ans = min(ans, cnt)
        cnt += 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >=N or nx < 0 or nx >=M:
                continue
            if visited[ny][nx] == 0 and m[ny][nx] ==1:
                 
                visited[ny][nx] =cnt
                q.append([ny,nx,cnt])
        
        #cnt = min(cnt, ans)
bfs(0,0)
print(ans)

# import sys
# N,M = list(map(int, input().split()))
# m = [list(map(int, input().split()[:-1])) for _ in range(N)]
# mp = []
# for i in m:
#     t = []
#     for j in str(i[0]):
#         t.append(int(j))
#     mp.append(t)
    
# dy = [0,0,-1,1]
# dx = [1,-1,0,0]

# def bfs(y,x):
#     global ans,visited
#     visited = [[0]*M for _ in range(N)]
#     visited[y][x] = 1 
#     q = []
#     cnt = 1
#     q.append([y,x,cnt])
#     ans = float('inf')
#     while q:
#         y,x,cnt = q.pop(0)
#         if y==N-1 and x ==M-1:
#             ans = min(ans, cnt)
#         cnt += 1
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if ny < 0 or ny >=N or nx < 0 or nx >=M:
#                 continue
#             if visited[ny][nx] == 0 and mp[ny][nx] ==1:
#                 visited[ny][nx] =cnt
#                 q.append([ny,nx,cnt])
# bfs(0,0)
# print(ans)