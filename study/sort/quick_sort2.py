arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <=1:
        return array
    
    #pivot setting
    pivot = array[0]
    tail = array[1:] #slicing except for pivot

    #left , right side setting
    left_side = [ x for x in tail if x <= pivot ]
    right_side = [ x for x in tail if x > pivot ]

    return quick_sort(left_side) + [ pivot ] + quick_sort(right_side)



print(quick_sort(arr))

# 오히려 정렬되어 있을 때 성능이 잘 안나온다.