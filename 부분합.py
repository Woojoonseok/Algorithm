# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:16:32 2020

@author: Seokwoojoon
"""

import sys
N,s = 5,0
num = [-7,-3,-2,5,8]

#N , s = list(map(int, input().split()))
#num =list(map(int, input().split()))
cnt =0
ans =0 
def dfs(K):
    global cnt, ans
    if K ==N:
        return 
    if num[K] + cnt == s:
        ans +=1 
    dfs(K+1)
    cnt += num[K] 
    dfs(K+1)
    cnt -= num[K]
dfs(0)
print(ans)
