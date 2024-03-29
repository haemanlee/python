x = int(input())


# dp 테이블 초기화 
d = [0] * 30001

for i in range(2, x+1):
    # 2,3,5로 나눠질 수 없는 것은 1을 빼고 연산횟수를 1 카운트 한다.
    d[i] = d[i-1] + 1
    # 2,3,5로 나눠지는 경우는 횟수와 현재 연산 횟수를 비교하여 최솟값으로 연산한다.
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[d//5] + 1)

print(d[x])