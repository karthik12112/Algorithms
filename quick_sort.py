def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() # 0
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    #print("greater {}").format(items_greater)
    #print("lower {}").format(items_lower)
    #print("==============================")
    x = quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
    print(x)
    return x

# items_greater = [5,6,8,9]

# items_lower = [0]
print(quick_sort([5,9,0]))
