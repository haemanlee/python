n, m = map(int, input().split())

#방문한 곳 체크하기 위한 2차원 행렬
d = [ m * [0] for _ in range(n)]
x, y, direction = map(int, input().split())

# 맵의 상태를 받아옴.
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 북쪽을 바라볼때는 북쪽으로 이동할 수 있는 좌표 이동이 (-1,0) 이다
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전하는 def
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 0
turn_count = 0
# 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        count += 1
        turn_count =0
        x = nx
        y = ny
    else:
        turn_count += 1
# 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한채로(direction) 한칸 이동하고 1단계로 돌아간다. 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
        turn_count = 0


print(count)