n, m = map(int, input().split())

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total+=x-mid
    # 최소 떡의 길이를 채워야 하므로 다음 이진탐색으로 넘어감. 높이 후보가 될 수 없음.
    if m > total:
        end = mid - 1
    # 최소 떡이 길이를 세웠으므로 높이의 후보가 될 수 있음.
    else:
        result = mid
        start = mid + 1

print(result)
