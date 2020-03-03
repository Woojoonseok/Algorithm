# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:24:26 2020

@author: Seokwoojoon
"""

L, C = list(map(int, input().split()))
string = list(map(str, input().split()))
temp_list = ['a','e','i','o','u']
#정렬
string.sort()
ans = [0]*20
def dfs(pos, prev, a,b): 
    if pos == L:
        #print(ans[:L])
        if a >=2 and b >=1:
            print(''.join(ans[:L]))
        return 
    for i in range(prev+1, C):
        ans[pos] = string[i]
        if string[i] in temp_list:
            dfs(pos+1, i,a,b+1)  
        else:
            dfs(pos+1, i,a+1,b)  
dfs(0, -1,0,0)
