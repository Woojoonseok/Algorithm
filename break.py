import copy
import sys
import itertools
sys.stdin = open("sample_input.txt", "r")
T = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for test_case in range(1,T+1):
    N,W,H = list(map(int, input().split()))
    m = [list(map(int,input().split())) for _ in range(H)]
    def shoot():
        while len(shoot_list):
            start_x = shoot_list.pop(0)
            start_y = -1
            for y in range(H):
                if m[y][start_x] != 0:
                    start_y = y
                    break
            if start_y == -1:
                continue
            #print(start_y,start_x)
            stack = []
            stack.append([start_y, start_x, m[start_y][start_x]])
            # BFS 시작
            while len(stack):
                cur = stack.pop(0)
                y = cur[0]; x = cur[1]
                val = cur[2]
                m[y][x] = 0
                for v in range(1, val):
                    for d in range(4):
                        ny = dy[d]*v + y
                        nx = dx[d]*v + x
                        if ny <0 or ny >= H or nx < 0 or nx >= W:
                            continue
                        if m[ny][nx] != 0 and m[ny][nx] != 1:
                            stack.append([ny,nx, m[ny][nx]])
                            m[ny][nx] = 0
                        if m[ny][nx] == 1:
                            m[ny][nx] = 0
            map_clean()
    def map_clean():
        temp = [[0] * W for _ in range(H)]
        for x in range(W):
            temp2 = [0]
            for y in reversed(range(H)):
                if m[y][x] ==0:
                    continue
                else:
                    temp2.append(m[y][x])
            for t in range(len(temp2)):
                temp[-t][x] = temp2[t]
        for y in range(H):
            for x in range(W):
                m[y][x] = temp[y][x]
    def get_block_number():
        cnt = 0
        for y in range(H):
            for x in range(W):
                if m[y][x] != 0:
                    cnt +=1
        return cnt

    ans = 999999
    map_backup = copy.deepcopy(m)
    for i in itertools.product(list(range(W)),repeat=N):
        #print(i)
        shoot_list = list(i)
        shoot()
        # 남은 벽돌 수 계산
        res = get_block_number()
        if res < ans:
            ans = res
            if ans == 0:
                break
        m = copy.deepcopy(map_backup)
    print('#{0} {1}'.format(test_case,ans))
