'''
먹이 우선순위 : 거리가 작은 것 -> x가 작은 것 -> y가 작은 것
'''

#먹이를 향해 이동하는 칸의 개수의 최솟값 구하는 함수
def bfs(shark_x,shark_y,feed_x,feed_y,shark_size):
    from collections import deque

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    d = deque()
    d.append((shark_x,shark_y,0)) # x, y, distance
    
    visited = [[0] * N for _ in range(N)]
    visited[shark_x][shark_y] = 1

    while d:

        x, y, distance = d.popleft()
        if [x, y] == [feed_x, feed_y]:
            return distance

        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0<=a<N and 0<=b<N and visited[a][b] == 0 and arr[a][b]<=shark_size:
                visited[a][b] = 1
                d.append((a, b, distance+1))
    return -1

#먹이를 찾는 함수, 크기가 작아도 해당 위치까지 갈 수 있어야함
def  search_feed(arr, shark_size):

    feed_list = []

    for i in range(N):
        for j in range(N):
            if 0< arr[i][j] < shark_size:
                
                distance = bfs(shark_x,shark_y,i,j,shark_size)
                if distance > 0:
                    feed_list.append((distance,i,j))
                else:
                    continue
    
    if feed_list:
        feed_list = sorted(feed_list, key = lambda x : (x[0],x[1],x[2]))
        return feed_list[0]
    
    return [-1, -1, -1]

# 먹이 먹고 레벨 업데이트       
def eating(feed_x,feed_y,shark_x,shark_y,shark_size,level, arr):
    
    arr[feed_x][feed_y] = 0
    level += 1

    if level == shark_size:
        shark_size += 1
        level = 0
    shark_x, shark_y = feed_x, feed_y

    return arr, shark_size, level, shark_x, shark_y


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                shark_x, shark_y, shark_size, level = i, j, 2, 0
                arr[i][j] = 0 

    time = 0

    while True:
        
        distance, feed_x, feed_y = search_feed(arr, shark_size) # 먹이를 찾는데,
        if distance > 0: # 먹을 수 있는 먹이가 있다면
            arr, shark_size, level, shark_x, shark_y =eating(feed_x,feed_y,shark_x,shark_y,shark_size,level, arr) 
            time += distance #먹으러 감
        else:
            break
    
    print(time)

    
            
