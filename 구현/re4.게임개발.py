n,m = map(int,input().split())


#n x m 배열 생성
d = [[0] * m for i in range(n)]    # 방문한 칸에 1 표시 

print(d)


x,y,direction = map(int,input().split())

d[x][y] = 1

array= []
for i in range(n):
    array.append(list(map(int,input().split())))

print(array)

# 북 동 남 서
dx = [-1,0, 1,0]
dy = [0, -1,0,1]

def turn_left():
    global direction 
    if direction == 0:
        direction =3
    else:
        direction -=1
    

count = 1 
turn_time =0
while True:
    if turn_time !=4:
        turn_left()
        next_x = x + dx[direction]
        next_y = y + dy[direction]

        if(array[next_x][next_y] == 1 or d[next_x][next_y] == 1 ):  #바다거나 방문했던 칸
            turn_time+=1
            continue
        else:
            x= next_x
            y= next_y
            d[x][y] = 1
            count+=1
            turn_time=0
    else: # turn_time == 4  => 네 방향 모두 못감
        # 한 칸 뒤로 
        turn_left()
        turn_left()
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        turn_left()
        turn_left()

        if array[next_x][next_y] == 1: # 바다인 칸  - 프로그램 종료
            break
        else: # 한칸 뒤로 이동
            x= next_x
            y= next_y
            turn_time = 0

print(count)

