
def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1) # [0,1,2]
    for i in indexing_length:
        min_value = i # 0 # 1
        for j in range(i+1, len(list_a)): 
            if list_a[j] < list_a[min_value]: # 7 < 6 # 0 < 7
                min_value = j
            if min_value != i: 
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
        print(list_a)
    return list_a



print(selection_sort([6,7,0]))
