from collections import deque


n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)

# 1,1에서 출발하여 0인 부분은 괴물이 있어서 지나갈 수 없다.
# 1인 부분만 지나갈 수 잇고 N,M 위치까지 이동한 최소 회수를 구하라(처음,끝도 카운트 한다)

# 4가지 방향을 미리 정의한다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs로 큐를 이용해서 인접한 노드를 먼저 탐색하는 방식으로 구현한다.
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 비어질때 까지 루프를 돌린다.
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계 라인을 확인한다.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 부분을 확인한다.
            if graph[nx][ny] == 0:
                continue
            # 길이를 + 하고, 인접한 노드를 큐에 추가한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))