input_data = input()

row_data = int(input_data[1])
# char를 인덱스 넘버로 바꾸는 방법
column_data =   int(ord(input_data[0])) - int(ord('a')) + 1

print(row_data, column_data)

steps = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]

count = 0
#결국 포인트는 꼼꼼하게 1<=x<=8, 1<=y<=8 확인하는 것이 포인트
for step in steps:
    next_row = row_data + step[0]
    next_column = column_data + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count+=1

print(count)