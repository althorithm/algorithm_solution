
def bfs(X,Y,answer):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    d.append((X,Y,0)) # x,y,t

    visited = [[0] * M for _ in range(N)]

    visited[X][Y] = 1

    while d:
        x,y,t = d.popleft()
        answer = max(answer,t)

        for k in range(4):
            a,b = x+dx[k] , y+dy[k]
            if 0<=a<N and 0<=b<M and visited[a][b] == 0 and arr[a][b] == 'L':
                visited[a][b] = 1
                d.append((a,b,t+1))
    return answer
    
import sys
from collections import deque

input = sys.stdin.readline

N , M = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(N)]

answer = -1

land_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            land_list.append((i,j))

for x,y in land_list:
    answer = bfs(x,y,answer)

print(answer)