# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:02:22 2020

@author: Seokwoojoon
"""

import sys
import copy
sys.stdin = open('2048.txt','r')

N = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#backup = 
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값 
# 위, 아래, 오른쪽, 왼쪽 
# 4^5 
ans =0 

def move():
    global m 
    temp = [[-1]*N for _ in range(N)]
    for x in range(N):
        flag = 0; target = - 1
        for y in range(N):
            #print(m[y][x])
            # 숫자가 없으면 그냥 넘어감 
            if m[y][x] ==0:
                continue
            if m[y][x] ==temp[target][x] and flag:
                flag = 0
                temp[target][x] *= 2
            else:
                target +=1 
                temp[target][x] = m[y][x]; flag= 1
        for i in range(target+1, N):
            target +=1 
            temp[target][x] = 0 
    m = copy.deepcopy(temp)
    
def rotate():
    global m 
    temp = copy.deepcopy(m)
    for y in range(N):
        for x in range(N):
            temp[y][x] = m[N-x-1][y]
    m= copy.deepcopy(temp)
    
def solve(cnt):
    global m, ans 
    if cnt ==5:
        ans = max(map(max, m))
        return
    for k in range(4):
        move()
        solve(cnt+1)
        rotate()
solve(0)
print(ans)

for i in zip(*m):
    print(i)





