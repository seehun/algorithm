graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9   # 0 ~ 8    0은 포함 x

def dfs (graph,v,visited):
    visited[v]= True   #방문처리
    print(v, end=' ')
    for i in graph[v]:  #인접한 노드들
        if not visited[i]:  # 방문처리되지 않았다면 
            dfs(graph,i,visited)

dfs(graph,1,visited)


    