start = input()

dx = [2,1,2,-2,-2,1,-1,-1]
dy = [1,2,-1,1,-1,-2,2,-2]

x = ['a','b','c','d','e','f','g','h']

count = 0
for i in range(8):
    if x.index(start[0:1]) + 1 + dx[i] > 0 and int(start[1:2]) + dy[i] > 0:
        count += 1

print(count)