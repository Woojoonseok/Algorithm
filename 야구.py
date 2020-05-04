# -*- coding: utf-8 -*-

#야구 
import sys
from itertools import combinations, permutations
sys.stdin = open('baseball.txt.', 'r')

N = int(sys.stdin.readline())
m = [[0]+ list(map(int,sys.stdin.readline().split() )) for _ in range(N)]
m.insert(0,[0]*10)
# 안타 1
# 2루타 2
# 3루타 3
# 홈런 4
# 아웃 0
def cal_score():
    global ans
    lu=[0]*4; out =0; score =0; strike =0;inn=1
    tasa =0 
    while inn <= N:
        ans = max(ans, score)
        if tasa ==9:
            tasa =0 
        if m[inn][tasun[tasa]] == 0:
            out += 1
        # 안타일 때 
        elif m[inn][tasun[tasa]] == 1:
            for i in range(3,0,-1):
                if lu[i]==1:
                    # 3루에 있을 때 득점 
                    if i==3:
                        lu[i]=0
                        score +=1
                    # 1,2루 이동--> 2,3 
                    else:
                        lu[i+1] = 1
                        lu[i] =0 
            lu[1] = 1 #  1루 채움 
        # 2루타 일 때
        elif m[inn][tasun[tasa]] == 2:
            for i in range(3,0,-1):
                if lu[i]==1:
                    # 2,3루 득점 --> 홈으로 
                    if i==3 or i==2:
                        lu[i]=0
                        score +=1
                    # 1루일 때 : 3루로 이동 
                    elif i==1:
                        lu[i+2] = 1
                        lu[i] = 0 
            lu[2] = 1
        # 3루타 일 때 
        elif m[inn][tasun[tasa]] == 3:
            for i in range(3,0,-1):
                if lu[i] == 1:
                    lu[i] =0 
                    score +=1
            lu[3] = 1
        # 홈런 일 때 
        elif m[inn][tasun[tasa]] == 4:
            for i in range(3,0,-1):
                if lu[i] ==1:
                    lu[i] =0 
                    score +=1 
            score +=1     
        if out ==3:
            inn += 1
            out =0
        tasa +=1 
        
ans =0 
tasun = list(range(9))


# for i in permutations(list(range(2,10)),8):
#     for idx, j in enumerate(i):
#         tasun[idx+1] = j 
#     tasun[0] = tasun[3]
#     tasun[3] = 1
#     if tasun[0]==5 and tasun[1]==6 and tasun[2] ==7:
#         pass
#     cal_score()
# print(ans)

order = [False]*10
select = [False]*10
select[4] = True
order[4] = 1
def dfs(n):
    global tasun
    if n == 10:
        #print(order)
        tasun = order[1:]
        print(tasun)
        #cal_score()
        return
    for i in range(1,10):
        if select[i] ==True:
            continue
        select[i] = True
        order[i] = n
        dfs(n+1)
        select[i] = False           
dfs(2)
print(ans)





