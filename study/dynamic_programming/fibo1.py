# 재귀적으로 메모이제이션(캐싱하여 기억)을 활용한 방식이다. 효율적으로 알고리즘을 짤 수 있다.
# 탑다운 방식 
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    #캐싱하여 처리
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
    