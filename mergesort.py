import time
s=time.time()
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        k =k+1

    while i < len(left):
        array[k] = left[i]
        i=i+1
        k=k+1

    while j < len(right):
        array[k] = right[j]
        j=j+1
        k =k+ 1

    return array
array = [40,2,5,10,5,50]
sorted_array = merge_sort(array)
print(sorted_array)
e=time.time()
print("time taken :",e-s)
