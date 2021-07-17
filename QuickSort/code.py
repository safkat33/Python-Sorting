# This is a sample Python script.

def swap(arr, a, b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp
    return arr


def partition(arr, l, r):
    pivot_index = r
    i = l
    j = l
    while j < r:
        if arr[j] < arr[pivot_index]:
            swap(arr, i, j)
            i += 1
        j += 1

    swap(arr, i, pivot_index)
    pivot_index = i
    return pivot_index


def quick_sort(arr, l, r):
    # Use a breakpoint in the code line below to debug your script.
    if l >= r:
        return arr

    pivot = partition(arr, l, r)

    quick_sort(arr, l, pivot-1)
    quick_sort(arr, pivot+1, r)

    return arr


arr_test = [2, 1, 6, 8, 9, 11, 7, 5, 3, 4, 10]

print(quick_sort(arr_test, 0, len(arr_test) - 1))
