n, m = map(int, input().split())

array = list(map(int,input().split()))

start = 0
end = max(array)
result = 0
while (start<=end):
    total = 0
    mid = (start+end) // 2

    for x in array:
        if x > mid:
            total += x - mid 

    # mid 기준으로 짜른 나머지 떡의 합이 m보다 작은 경우
    if total < m:
        end = mid - 1
    # mid 기준으로 짜른 나머지 떡의 합이 m보다 큰 경우
    else:
        result = mid
        start = mid + 1

print(result)