def dfs(graph, v, visited):
    #방문체크
    visited[v] = True

    print(v)
    #graph 인접한 노드를 방문하는 재귀함수를 구현한다.
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)



graph = [
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
visited = [False] * 9

dfs(graph, 1, visited)