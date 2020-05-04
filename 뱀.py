# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:58:33 2020

@author: Seokwoojoon
"""

import sys
sys.stdin = open('뱀.txt','r')
N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = [list(map(int,sys.stdin.readline().split())) for i in range(k)]
L = int(sys.stdin.readline())
direction = [sys.stdin.readline().split() for i in range(L)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

for i in direction:
    i[0] = int(i[0])
m = [[0]*(N+1) for _ in range(N+1)]
for i in apple:
    y, x = i
    m[y][x] = 1
m[1][1] = 2 
# 전체 틀 
done = True
t = 0
q = [] 
q.append([1,1]) 
cur_dir = direction.pop(0)
d = 0
while done:
    # 방향 정하기
    y, x = q[-1]
    if cur_dir[0] == t:
        # 오른 쪽 
        if cur_dir[1] =='D':
            d = (d+1)%4
        # 왼쪽
        else:
            d = (d-1)%4
        if len(direction):
            cur_dir = direction.pop(0)
    # 이동 
    ny = dy[d] + y
    nx = dx[d] + x 
    if 1 <= ny <= N and 1 <= nx <= N:
        # 몸통에 닿았을 때 
        if m[ny][nx] == 2:
            print(t+1)
            break
        # 사과가 아닐 때 y,x를 지움  
        if m[ny][nx] != 1:
            sy, sx = q.pop(0)
            m[sy][sx] = 0 
        q.append([ny,nx])
        # 
        for i in q:
            yy = i[0]; xx = i[1]
            m[yy][xx]= 2 
    # 밖으로 나갔을 때 종료
    else:
        print(t+1)
        break
    t += 1 
        
    