
n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input())))

print(array)


count = 0
# 상하좌우를 살펴보고 아직도 갈 수 있다면 계속 0을 찾아서 이동하는 재귀함수 구현.
def dfs (array, x, y):
# terminate
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

# recursive
    if array[x][y] == 0:
        array[x][y] = True
        
        dfs(array, x, y-1)
        dfs(array, x, y+1)
        dfs(array, x-1, y)
        dfs(array, x+1, y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(array, i, j) == True:
            count+=1


print(count)