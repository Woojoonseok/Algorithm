# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:18:13 2020

@author: Seokwoojoon
"""

import sys
sys.stdin = open('구슬탈출.txt')
N, M = list(map(int, sys.stdin.readline().split()))
m = [list(sys.stdin.readline().strip())  for _ in range(N)]
# 구슬 2개가 한꺼번에 움직여야 함 --> MxN x MxN  한꺼번에 체크 
visited = [ [[[False]*M for _ in range(N)]  for _ in range(M)] for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]
q = [] 
for y in range(N):
    for x in range(M):
        if m[y][x] =='R':
            ry , rx = y , x
        elif m[y][x] == 'B':
            by, bx = y , x
q.append([ry,rx,by,bx,0])
visited[ry][rx][by][bx] = True

def move(y , x , dy, dx, c):
    while m[y+dy][x+dx] != '#' and m[y][x] !='O':
        y += dy
        x += dx
        c += 1
    return y, x, c 

def bfs():
    while q:
        ry , rx , by, bx,dis = q.pop(0)
        if dis >= 10:
            break
        for d in range(4):
            nry, nrx, rc = move(ry, rx, dy[d], dx[d], 0)
            nby, nbx, bc = move(by, bx, dy[d], dx[d], 0)
            
            #구멍에 빠졌을 때 - 파란색을 먼저 처리해준다 ( 동시에 빠졌을 때 )
            if m[nby][nbx] =='O':
                continue
            if m[nry][nrx] == 'O':
                print(dis+1)
                return 

            # 겹쳤을 때 
            if nry == nby and nrx == nbx:
                if rc > bc:
                    nry -= dy[d]
                    nrx -= dx[d]
                else:
                    nby -= dy[d]
                    nbx -= dx[d]
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append([nry, nrx, nby, nbx, dis+1])
    print(-1)
bfs()                    
        
    