# This is a sample Python script.

# def swap(arr, a, b):
#     temp = arr[b]
#     arr[b] = arr[a]
#     arr[a] = temp
#     return arr


def partition(arr, left, right):
    pivot_index = right
    i = left
    j = left
    while j < right:
        if arr[j] < arr[pivot_index]:
            # swap(arr, i, j)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    # swap(arr, i, pivot_index)
    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    pivot_index = i
    return pivot_index


def quick_sort(arr, left, right):
    # Use a breakpoint in the code line below to debug your script.
    if left >= right:
        return arr

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)

    return arr


arr_test = [2, 1, 6, 8, 9, 11, 7, 5, 3, 4, 10]


class SortArray:
    def __init__(self, array_test):
        self.arr_test = array_test
    print("Un-sorted Array", arr_test)
    sorted_array = quick_sort(arr_test, 0, len(arr_test) - 1)
    print("Sorted Array", sorted_array)
