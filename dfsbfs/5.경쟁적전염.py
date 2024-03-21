# 344

n =3   # n x n
k =3   # 바이러스 종류 1 ~ 3

data = [
    [1,0,2],
    [0,0,0],
    [3,0,0]
]

def print_data():
    print('data')
    length = len(data)
    for i in range(length):
        print(data[i],end='\n')
    print()

s= 2
x,y = 3,2


temp= [[0]*n for i in range(n)]

def print_temp():
    print('temp')
    length = len(temp)
    for i in range(length):
        print(temp[i],end='\n')
    print()


dx=[-1,1,0,0]
dy=[0,0,-1,1]
def virus(x,y,a):
    # a -> 종류
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
            continue
        
        if temp[x][y]==a and data[nx][ny]==0:
            data[nx][ny] = a




for time in range(s):
    for i in range(n):
        for j in range(n):
            temp[i][j] = data[i][j]


    for vi in range(1,k+1):  # 1 ~ k
        for i in range(n):
            for j in range(n):
                virus(i,j,vi)

print_data()

if data[x-1][y-1]==0:
    print(0)
else:
    print(data[x-1][y-1])