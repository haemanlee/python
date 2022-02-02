n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
target_list = list(map(int, input().split()))


# target, start, end 모두 서수 이다.
def binary_search(array, target, start, end):
    if start > end:
        return False    

    mid = (start + end) // 2
    if target == array[mid]:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in target_list:
    if binary_search(array, i, 0, n-1) == True:
        print('yes', end=' ')
    else:
        print('no', end=' ')

