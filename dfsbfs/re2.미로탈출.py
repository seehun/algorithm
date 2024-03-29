# 152

from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))


# 상 하 좌 우 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):

    q= deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):  # 현재 위치에서 4방향
            nx = x+ dx[i]
            ny = y+ dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

    return graph[n-1][m-1]




print(bfs(0,0))
print(graph)