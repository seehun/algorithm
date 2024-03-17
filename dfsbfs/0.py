from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):

    q = deque([(x,y)])

    while q:
        x,y = q.popleft()

        for i in range(4):  # 상 하 좌 우
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

bfs(0,0)
print(graph)
print(graph[n-1][m-1])