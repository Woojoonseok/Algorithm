# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:56:52 2020

@author: Seokwoojoon
"""

import sys
with open("새로운게임.txt",'r') as f:
    N, K  = list(map(int, f.readline().split()))
    m = [list(map(int, f.readline().split())) for _ in range(N)]
    board = [[[] for _ in range(N)] for _ in range(N)]
    pos = [-1]
    dir = [-1]
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    for n in range(1,K+1):
        y,x,d = map(int, f.readline().split())
        y-=1 ; x -=1; d -=1 
        board[y][x].append(n)
        pos.append([y,x])
        dir.append(d)


def go():
    for n in range(1,K+1):
        y, x = pos[n]
        ny, nx, dir[n] = ny_nx_nd(n)
        if y ==ny and x == nx: continue
        idx = board[y][x].index(n)
        move(y,x,ny,nx,idx)
        elements = board[y][x][idx:]
        board[y][x] = board[y][x][:idx]
        if m[ny][nx] ==0:
            board[ny][nx] += elements[:]
        elif m[ny][nx] ==1:
            board[ny][nx] += elements[::-1]
        if len(board[ny][nx])>=4:
            return True
    return False
        

def move(y,x,ny,nx,idx):
    for n in board[y][x][idx:]:
        pos[n] = [ny, nx]
        
def ny_nx_nd(n):
    (y,x), d = pos[n], dir[n]
    if check(y + dy[d], x+dx[d]):
        y, x = y + dy[d], x + dx[d]
    else:
        d ^=1
        if check(y+dy[d], x+dx[d]):
            y, x = y+dy[d], x+ dx[d]
    return (y,x,d)

def check(y,x):
    if not (0 <= y < N and 0 <= x < N): return False
    if m[y][x]==2: return False
    return True

turn =0 
while True:
    turn +=1 
    if turn == 1001:
        print(-1)
        break
    if go():
        print(turn)
        break
