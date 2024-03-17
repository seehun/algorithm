# 339

from collections import deque

n,m,k,x = 4,4,2,1


graph = [ [] for i in range(n+1) ]
print(graph)
for i in range(m):
    start,end = map(int,input().split())
    graph[start].append(end)

# print(graph)

d = [-1] * (n+1)
d[0]=0
d[x]=0

q= deque([x])  

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if d[next_node] ==-1:
            d[next_node] = d[now]+1 
            q.append(next_node)

print(d)

cities = []
for i in range(len(d)):
    if d[i]== k:
        cities.append(i)

print(cities)


