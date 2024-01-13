from collections import deque
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
for i,j in enumerate(arr):
    if 9 in j:
        sx,sy= i,j.index(9)



level = 2
cnt = 2
time = 0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visted=[[0]*N for _ in range(N)]
visted[sx][sy]=1
d = deque()
d.append([sx,sy,0])
ans =[]

while d:
    X,Y,count= d.popleft()
    for i in range(4):
        a=X+dx[i]
        b=Y+dy[i]
        if 0<=a<N and 0<=b<N:
            if visted[a][b]==0 and arr[a][b]<=level:
                visted[a][b]=1
                if 0<arr[a][b]<level:
                    ans.append([a,b,count+1])
                else:
                    d.append((a,b,count+1))

           
    print(d,ans)
    if not d:      
        if ans:
            
            ans= sorted(ans,key=lambda x: (x[2],abs(x[0]-sx)+abs(x[1]-sy),x[0],x[1]))
            
            idx,idy = ans[0][0],ans[0][1]
         
            time+=ans[0][2]
            cnt-=1
            arr[sx][sy]=0
            arr[idx][idy]=9
            sx,sy = idx,idy
            d=deque()
            d.append([idx,idy,0])
            ans=[]
            # count=[[0]*N for _ in range(N)]
            visted=[[0]*N for _ in range(N)]
            visted[sx][sy]=1

        if cnt==0:
            level+=1
            cnt=level

print(time)
    