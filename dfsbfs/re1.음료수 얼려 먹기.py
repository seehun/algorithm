#p149

n,m =  map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))


def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] ==1:
        return False

    elif graph[x][y] ==0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True




count = 0 

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count+=1

print(count)



