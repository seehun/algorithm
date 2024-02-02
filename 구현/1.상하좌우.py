n = int(input())

move_list = list(input().split())

direction = ['L','R','U','D']
dx=[0,0,-1,1]
dy=[-1,1,0,0]

pos = [1,1]


# find index sol
# direction = ['l','r']
# direction.index('l')
#  -> 0

for move in move_list:
    i = direction.index(move)
    x = dx[i]
    y=  dy[i]
    if(pos[0]+x<1 or pos[0]+x>n or pos[1]+y<1 or pos[1]+y>n):
        continue
    else:
        pos[0] +=x
        pos[1] +=y

print(pos)
