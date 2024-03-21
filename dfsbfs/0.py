n,m = 7,7

data =[
    [2,0,0,0,1,1,0],
    [0,0,1,0,1,2,0],
    [0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0]
]  # 맵

temp = [ [0]*m for i in range(n) ]


dx=[-1,1,0,0]
dy=[0,0,-1,1]
def virus(x,y):
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
            continue
        else:
            if temp[nx][ny]==0:
                temp[nx][ny] = 2
                virus(nx,ny)
    
# virus(0,0)
# print(data)
result=0
def get_score():
    safe =0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                safe+=1
    return safe



def dfs(count):
    global result
    if count==3:  # 바이러스 , 점수 세기
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] ==2:
                    virus(i,j)
        result = max(get_score(),result)
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] ==0:
                data[i][j] = 1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)