# 327

n=10   # 보드 크기
k=3   # 사과 갯수

apples=[
    [1,5],
    [1,3],
    [1,2],
    [1,6],
    [1,7]
]

l = 3 # 방향 변환 횟수
moves=[
    [8,'D'],
    [10,'D'],
    [11,'D'],
    [13,'L']
]

mapData = [ [0]*n for i in range(n) ]
def printMap():
    mapLen = len(mapData)
    for i in range(mapLen):
        print(mapData[i],end='\n')

for apple in apples:
    x,y = apple
    mapData[x-1][y-1] = 1

printMap()

direction = 0  # 첨엔 오른쪽 봄
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def turnLeft():
    global direction 
    if direction==3:
        direction =0
    else:
        direction +=1   


def turnRight():
    global direction
    if direction==0:
        direction =3
    else:
        direction -=1

time =0

# x,y = 0,0  # 0,0에서 출발

def game(x,y):
    global time
    mapData[x][y] = 2 # 뱀이 차지하는 영역에 2 표시

    q= [(x,y)]  # 뱀의 몸

    for move in moves:  

        for head_move in range(move[0]):
            nx = x+ dx[direction]
            ny = y+ dy[direction]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
                return
            if mapData[nx][ny] ==2:  # 자기자신
                return 
            if mapData[nx][ny] ==1:  # 사과를 먹으면
                mapData[nx][ny] =0 # 사과가 없어지고
                # mapData[x][y] = 2  # 자기자신의 꼬리는 유지
                # 머리 이동
                x=nx  
                y=ny
                q.append((x,y))
                time+=1
                continue
            if mapData[nx][ny] ==0 : # 사과가 없으면
                #꼬리가 있던 자리에 0을 표시 
                px,py = q.pop(0)
                mapData[px][py] =0
                # 머리 이동
                x=nx  
                y=ny
                mapData[x][y] =2
                q.append((x,y))
                time+=1
                continue
        print(time)

        if move[1]=='L':
            turnLeft()
        if move[1]=='D':
            turnRight()
            



game(0,0)
print(time+1)
printMap()


# 문제 잘못 파악 
# 8 D   ,  10 D 
# 8번 이동하고 D , 10번 이동하고 D가 아니라 
# 게임시작 8초 후  D, 그로부터 2초뒤에(게임시작 10초)에 D
# 뱀은 항상 움직임 