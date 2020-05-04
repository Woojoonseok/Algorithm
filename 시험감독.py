# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:59:50 2020

@author: Seokwoojoon
"""

import sys
sys.stdin = open('시험감독.txt','r')
#inp = sys.stdin.readline()
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
B, C = list(map(int, sys.stdin.readline().split()))

res = 0 
for i in range(N):
    num[i] -= B
    res +=1 
    if num[i] > 0:
        temp = int(num[i]/C)
        if num[i]%C !=0:
            temp +=1 
        res += temp 
print(res)