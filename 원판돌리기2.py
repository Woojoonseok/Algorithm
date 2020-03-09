# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:38:27 2020

@author: Seokwoojoon
"""

# 원판 돌리기 
import copy
import sys
sys.stdin = open('onepan.txt','r')


N,M,T = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
instruction = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

# 
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def rotate(x,d,k):
    # d가 0일 때 : 시계, 1일 때 반시계
    k %= M 
    temp = info[x]
    # 반시계 
    if d==1:
        for i in range(k):
            temp.append(temp.pop(0))
    # 시계 
    elif d==0:
        for i in range(M-k):
            temp.append(temp.pop(0))
    info[x] = temp

def cal_mean():
    Sum = sum(sum(info,[]))
    if Sum ==0:
        return
    cnt =0 
    for y in range(N):
        for x in range(M):
            if info[y][x] !=0:
                cnt +=1 
    mean = Sum / cnt 
    for y in range(N):
        for x in range(M):
            if info[y][x] ==0:
                continue
            if info[y][x] > mean:
                info[y][x] -=1
            elif info[y][x] < mean:
                info[y][x] += 1 

def bfs():
    temp = copy.deepcopy(info)
    q = []
    q.append([0,0])
    visited = [[0]*M for _ in range(N)]
    flag = False 
    while q:
        cur = q.pop(0)
        y = cur[0]; x = cur[1]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            # 오른쪽 
            if x ==0 and d == 1:
                nx = M-1
            #왼쪽 
            if x== M-1 and d== 0:
                nx = 0
            if ny <0 or ny >=N or nx <0 or nx >=M:
                continue
            if visited[ny][nx] ==0:
                q.append([ny,nx])
                visited[ny][nx] = 1 
            if info[ny][nx] == info[y][x] and info[y][x] !=0 :
                temp[ny][nx] = -1
                temp[y][x] = -1
                flag = True

    for y in range(N):
        for x in range(M):
            if temp[y][x] == -1:
                info[y][x] =0
    return flag 
    
# 0) 돌릴 원판 찾기 
for i in instruction:
    x = i[0]; d = i[1]; k= i[2]
    # x의 배수 찾기
    onepan_list = [x*(i+1)-1 for i in range(len(info)//x)]
    for xi in onepan_list:
        # 1) 원판 회전
        rotate(xi,d,k)
    # 2) BFS 로 인접한 숫자 찾고 지우기  
    if bfs()== False:
        # 2-2) 없는 경우
        cal_mean()

# 3) 합 구하기
print(sum(sum(info,[])))
