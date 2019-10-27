import sys
import itertools
import copy
sys.stdin = open('sample_input.txt','r')
from collections import Counter
T = int(input())
dy = [1,-1,0,0]
dx=  [0,0,-1,1]
for test_case in range(1,T+1):
    if test_case==2:
        break
    N, W, H = list(map(int, input().split()))
    m = [list(map(int,input().split())) for _ in range(H)]
    print(m)
    # W 개 중에N 개 선택
    for i in itertools.combinations(list(range(W)),N):
        print(i)
        start_list = list(i)
        # BFS
        # 맞는 곳 찾아서 BFS 시작
        while len(start_list):
            start_x = start_list.pop(0)
            start_y = -1
            stack = []
            for y in range(W):
                if m[y][start_x] != 0:
                    start_y = y
                    break
            if start_y == -1:
                continue
            # BFS 시작할 곳 찾음
            #visited = [[0]*W for _ in range(H)]
            #visited[start_y][start_x] = 1
            cnt =0
            stack.append([start_y, start_x, m[start_y][start_x]])
            while len(stack):
                cur = stack.pop(0)
                y = cur[0]
                x = cur[1]
                val = cur[2]
                for d in range(4):
                    for v in range(1,val+1):
                        ny = dy[d]*v + y
                        nx = dx[d]*v + x
                        if ny < 0 or ny >= H or nx <0 or nx >= W:
                            continue
                        if m[ny][nx] ==1:
                            m[ny][nx] = 0
                            continue
                        if m[ny][nx] != 0 and m[ny][nx] != 1:
                            stack.append([ny, nx, m[ny][nx]])
                            m[ny][nx] = 0
