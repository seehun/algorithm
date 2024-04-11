from collections import deque

n=2
l,r = 20,50

graph=[
    [50,30],
    [20,40]
]


dx=[-1,1,0,0]
dy=[0,0,-1,1]


def process(x,y,index):
    
    total_people =graph[x][y]
    unity_num=1
    unity_country=[(x,y)]
    union[x][y] = index

    q = deque([(x,y)])

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(graph[x][y] - graph[nx][ny]) <= r:
                    q.append((nx,ny))
                    total_people+=graph[nx][ny]
                    unity_num+=1
                    unity_country.append((nx,ny))
                    union[nx][ny] =index
    
    for i,j in unity_country:
        graph[i][j] = total_people//unity_num


total_count = 0 
while True:
    index =0   #연합 이름
    union = [ [-1] *n for i in range(n) ]

    for i in range(n):
        for j in range(n):
            if union[i][j]== -1:
                index+=1
                process(i,j,index)
    
    if index == n*n:
        break
    total_count+=1
    print(graph)


print(total_count)