# -1을 하거나 k로 나눈다.
# 두개의 경우의 수를 거쳐서 1이되면 중지한다.
# n은 나누거나 -1을 할 대상이다
# k은 나눠지는 값이다.
n, k = map(int, input().split())

count = 0
while True:

  # -1할 대상을 미리 빼놓는다.
  target = (n // k) * k
  n = target
  count += n - target

  # n/k으로 나눠지는 경우를 카운트 한다.
  if n < k:
    break

  count += 1
  n //= k

# n < k 이후에는 k로 나눠지지 않고 n-1만큼 -1을 처리한다.
count += n-1     
print(count)
