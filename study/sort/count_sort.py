arr = [7,5,9,0,3,1,6,2,4,8]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(arr)+1)

# index에 해당하는 count를 올려준다.
for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')


