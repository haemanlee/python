arr = [7,5,9,0,3,1,6,2,4,8]

# 삽입정렬은 i = 1부터 시작을 통해서 iterate를 돌리고 끝에서부터 -1 감소하는 방식으로 swap을 시작한다.
for i in range(1, len(arr)):
    # i 부터 시작해서 작은수가 뒤에 있을때 swap을 시작해야 한다.
    for j in range(i,0,-1):
        # 내림차순이어야 하므로 
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

print(arr)

# 일반적으로 퀵소트보다는 시간복잡도가 높지만 정렬되있는 상태라면 퀵소트보다 강력한 속도를 낼 수 있다.