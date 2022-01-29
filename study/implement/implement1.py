# L
# R
# U
# D
n = int(input())
arr = list(map(str, input().split()))

x = 1
y = 1

print(n)
print(arr)
for str in arr:
    if str == 'L':
        if y>1:
            y-=1
    elif str == 'R':
        if y<5:
            y+=1
    elif str == 'U':
        if x>1:
            x-=1
    elif str == 'D':
        if x<5:
            x+=1

print(x, y)
