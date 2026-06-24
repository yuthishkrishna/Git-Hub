def quick_sort(integers):
    if len(integers) <= 1:
        return integers   # return the list itself

    pivot_value = integers[0]
    less = [x for x in integers if x < pivot_value]
    equal = [x for x in integers if x == pivot_value]
    greater = [x for x in integers if x > pivot_value]

    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([20, 3, 14, 1, 5]))