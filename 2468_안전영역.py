def bfs(X,Y):

    d = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[X][Y] = 1

    d.append((X,Y))

    cnt = 0

    while d:
        x,y = d.popleft()

        for k in range(4):
            a,b = x+dx[k],y+dy[k]

            if 0<=a<N and 0<=b<N and visited[a][b] == 0 and temp[a][b] == 1:
                d.append((a,b))
                visited[a][b] = 1
                cnt+=1 
    
    

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline 

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

M = 0
for i in range(N):
    for j in range(N):
        M = max(M,arr[i][j])

depth_list = [i for i in range(M+1)]

answer_list = []
for depth in depth_list:
    temp = [[0] * N for _ in range(N)]
    
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] >depth:
                temp[i][j] = 1
    

    visited = [[0] * N for _ in range(N)]
    
    safezone = 0 
    for p in range(N):
        for q in range(N):
            if visited[p][q] == 0 and temp[p][q] == 1:
                bfs(p,q)
                safezone += 1

    answer_list.append(safezone)

print(max(answer_list))