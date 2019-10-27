import sys
import copy
sys.stdin = open('sample_input.txt','r')
from collections import Counter
T = int(input())
# 하, 우, 상, 좌
dy = [1,0,-1,0]
dx = [0,1,0,-1]
for test_case in range(1,T+1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    def wall(d):
        if d==0: return 2
        elif d==1: return 3
        elif d==2:
            return 0
        elif d==3:
            return 1
    def hit_block(val, d):
        if val == 1:
            if d == 3:
                return 2
            elif d==0:
                return 1
            elif d==1:
                return 3
            elif d==2:
                return 0
        elif val==2:
            if d==0:
                return 2
            elif d==1:
                return 3
            elif d==2:
                return 1
            elif d==3:
                return 0
        elif val ==3:
            if d==0:
                return 2
            elif d==1:
                return 0
            elif d==2:
                return 3
            elif d==3:
                return 1
        elif val ==4:
            if d==0:
                return 3
            elif d==1:
                return 2
            elif d==2:
                return 0
            elif d==3:
                return 1
        else:
            if d==0:
                return 2
            elif d==1:
                return 3
            elif d==2:
                return 0
            elif d==3:
                return 1

    def w_hall(y, x, val):
        ny, nx =0,0
        for i in w_hole:
            if val == i:
                for j in w_hole[val]:
                    if j != [y,x]:
                        ny = j[0]
                        nx = j[1]
        return [ny, nx]

    def dfs(d):
        global ans
        score = 0
        ny, nx = y, x
        while True:
            ny += dy[d]
            nx += dx[d]
            # Score 최대 값 갱신
            if ans < score:
                ans = score
                break
            # 초기 위치로 돌아갔을 때 break
            if ny==y and nx ==x:
                break
            # 벽에 닿았을 때 방향 반대, score +1
            if ny >= N or ny < 0 or nx >= N or nx <0:
                d = wall(d)
                score +=1
            else:
                # 블록에 닿았을 때
                if 1 <= m[ny][nx] <= 5:
                    d =hit_block(m[ny][nx], d)
                    score +=1
                # 웜홀 일 때
                elif 6<= m[ny][nx] <= 10:
                    ny, nx = w_hall(ny, nx, m[ny][nx])
                #블랙홀일 때
                elif m[ny][nx] == -1:
                    break

    # 벽저장
    #black_hole = []
    block = []
    w_hole ={}
    ans =0

    for y in range(N):
        for x in range(N):
            if m[y][x] !=0 and m[y][x] < 6:
                block.append([y,x])
            elif m[y][x] !=0 and m[y][x] >=6:
                w_hole[m[y][x]] = w_hole.get(m[y][x],[]) + [[y,x]]
    for y in range(N):
        for x in range(N):
            # if y==2 and x ==3:
            #     print('d')
            if m[y][x] == 0:
                for d in range(4):
                    dfs(d)
    print('#{0} {1}'.format(test_case,ans))


