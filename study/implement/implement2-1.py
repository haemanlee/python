# 완전 탐색 유형
# 100만개 이하이므로 완저탐색으로 풀어도 문제 없다.
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


