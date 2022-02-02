n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

print(arr)

arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i], end=' ')