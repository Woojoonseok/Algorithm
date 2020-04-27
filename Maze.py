# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:15:05 2020

@author: Seokwoojoon
"""
import copy
import os
import sys
from itertools import permutations
sys.stdin = open('Maze.txt', 'r')
maze = [ list(map(int, sys.stdin.readline().split())) for _ in range(25)]
maze_2 = [ [[ 0 for _ in range(5)] for _ in range(5)] for i in range(5)] 
temp = [ [[0 for _ in range(5)] for _ in range(5)] for i in range(5)] 
for z in range(5):
    for y in range(5):
        for x in range(5):
            maze_2[z][y][x] = maze[z*5+y][x]
dz = [-1, 1, 0,  0,  0, 0]
dy = [0,  0, 0,  0, -1, 1]
dx = [0,  0, 1, -1,  0, 0]
min_val = float('inf')
def bfs():
    global min_val,maze_2
    q = []
    cnt = 0
    q.append([0,0,0,cnt])
    visitied = [ [[-1 for _ in range(5)] for _ in range(5)] for i in range(5)]
    visitied[0][0][0] =  0
    while q:
        cur = q.pop(0)
        z,y,x= cur[0],cur[1],cur[2]
        if z==4 and y ==4 and x==4:
            min_val = min(visitied[z][y][x], min_val)
            if min_val == 12:
                return 
            return 
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5:
                continue
            if visitied[nz][ny][nx] == -1 and maze_2[nz][ny][nx] !=0:
                visitied[nz][ny][nx] = visitied[z][y][x] + 1 
                q.append([nz,ny,nx,cnt])            
def rotate(num):
    global maze_2
    change = [[0,0,0,0,0] for i in range(5)]
    for r in range(5):
        for c in range(5):
            change[c][5-1-r]  =  maze_2[num][r][c]
    maze_2[num] = change

def maze(cnt):
    if cnt ==5:
        if maze_2[4][4][4]:
            bfs()
        return 
    for i in range(4):
        if maze_2[0][0][0]:
            maze(cnt+1)
        rotate(cnt)
    
backup = copy.deepcopy(maze_2)
for i in permutations(range(5),5):
    for k in range(5):
        temp[i[k]] = backup[k]
        maze_2 = copy.deepcopy(temp)
    maze(0) 
print(min_val if min_val != float('inf') else -1)
