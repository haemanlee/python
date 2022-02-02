n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1

m = int(input())
target_list = list(map(int, input().split()))

for j in target_list:
    if array[j] == 1:
        print('yes', end= ' ')
    else:
        print('no', end=' ')
        