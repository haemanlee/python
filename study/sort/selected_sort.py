from re import M


arr = [3,4,5,6,1,3]

# 선택 정렬로 arr루프를 돌려서 가장 작은 iterate하면서 가장 작은 수와 swap을 진행한다.

for i in range(0, len(arr)):
    #min index이 일단 최소값이라고 가정하고 define한다.
    min_index = i
    for j in range(i+1, len(arr)):
        # 만약 min_index보다 작은 j가 있을 경우 swap이 일어난다.
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)