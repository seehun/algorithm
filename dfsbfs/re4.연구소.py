# 341

# 완탐, dfs

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

temp = [ [0]*m for i in range(n) ]  # 벽을 설치한 뒤 맵

result = 0  # 안전지대 개수

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 바이러스 퍼지는 함수 ,  벽을 다 세운 후에 실행
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx>=n or nx<=-1 or ny>= m or ny<=-1:
            continue  # return False 하면 안됨 -> 함수 자체가 종료 
        
        else:
            if temp[nx][ny] ==0:
                temp[nx][ny] = 2
                virus(nx,ny)




# 점수 내는 함수
def get_score():
    score = 0 
    for i in range(n):
        for j in range(m):
            if temp[i][j] ==0:
                score+=1
    return score


def dfs(count):
    global result

    if count ==3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] ==2:
                    virus(i,j)
        
        result = max(result, get_score())
        return


    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j] =1
                count+=1
                dfs(count)
                # map을 원상 복귀
                data[i][j] = 0
                count-=1


dfs(0)
print(result)