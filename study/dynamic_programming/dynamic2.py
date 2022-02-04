n = int(input())
k = list(map(int,input().split()))

d = [0] * 100

# max(식량창고와 떨어진 것(i-2) + 현재 i의 식량, i-1의 최대값)
d[0] = k[0]
d[1] = max(k[0],k[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])