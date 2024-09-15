def selection(array):
    n=len(array)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if array[j] < array[min]:
                min=j
            if i!=min:
                array[i],array[min]=array[min],array[i]
    return array
array=[10,56,12,23,2]
print(selection(array))

