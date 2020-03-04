# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:45:19 2020

@author: Seokwoojoon
"""

import sys
import copy
#sys.stdin = open('castle_defense.txt','r')
N,M,D = list(map(int, sys.stdin.readline().split()))
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
m.append([0]*M)
backup = copy.deepcopy(m)
archer_list = list(range(M))
archer = []
dy = [0,0,1,-1]
dx = [1,-1,0,0]
shoot_list = []
ans =0 
cnt =0 
# 궁수 공격
def attack(pos):
    # input : 현재 궁수 위치 
    # output: None
    # 적군 위치를 찾아서 임시 배열에 표시 
    global shoot_list,backup, cnt
    y = N; x = pos
    temp = []
    # 적군ㅇ
    for i in range(N+1):
        for j in range(M):
            if backup[i][j] == 1 and abs(i-N) +  abs(j-pos) <= D:
                temp.append([i,j,abs(i-N) +  abs(j-pos)])
    
    # 가장 가까운놈 부터 쏨 
    # d 최소 찾기 --> 중복 일때 왼쪽 고름 
    if len(temp) >1:
        find_min_d = float('inf')
        #Counter(temp, key=lambda x:x[2])
        temp.sort(key = lambda x:x[2])
        d_min = temp[0][2]
        while True:
            if temp[-1][2] != d_min:
                temp.pop()
            else:
                break
        
        if len(temp)==0:
            return  
    min_val =  float('inf')
    temp2 = [0,0]
    if len(temp)>1:
        for i in temp:
            if min_val > i[1]:
                min_val = i[1]
                temp2[0] = i[0]
                temp2[1] = min_val
        shoot_list.append(temp2)
    else:
        shoot_list.extend(temp)
        
        
    
def map_move(m):
    m.pop(-2)
    m.insert(0,[0]*M)
# M개 중 3개를 뽑음
def dfs(n):
    global archer_list, archer, shoot_list, ans, backup, cnt
    cnt =0 
    if len(archer)==3:
        #print(archer)
        #배치
        # if archer == [1,2,3]:
        #     print('d')
        # 맵초기화
        backup = copy.deepcopy(m)
        game_end= False
        while True:
            if game_end:
                break
            # 적이 화살 맞은 위치 초기화 
            shoot_list = []
            for a in archer:
                backup[N][a] = 9 
                attack(a)
            for i in shoot_list:
                #print(i)
                #i = i[0]
                cnt += 1
                # 같은 적을 쐈을 때
                if backup[i[0]][i[1]] ==0:
                    cnt -= 1
                else:
                    backup[i[0]][i[1]] =0 
            #맵 이동 
            map_move(backup)
                #game_end = True
            # 적을 다 잡았을 때 
            if sum(sum(backup[:-1],[]))==0:
                game_end = True
            ans = max(cnt, ans)
        #print(ans)
        return
    
    for i in range(n,M):
        archer.append(i)
        dfs(i+1)
        archer.pop()

dfs(0)
print(ans)
