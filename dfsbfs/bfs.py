from collections import deque

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

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True  # 현재 노드 방문처리

    while queue:
        # 큐에서 원소를 하나 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,1,visited)

