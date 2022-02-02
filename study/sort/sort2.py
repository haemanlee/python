n = int(input())

array = []
for i in range(n):
    (x, y) = input().split()
    array.append((x,int(y)))

# def setting(data):
#     return data[1]


# array = sorted(array, key=setting, reverse=False)

array = sorted(array, key=lambda student: student[1])

print(array)
