# This is a sample Python script.


def merge_sort(arr):
    # Use a breakpoint in the code line below to debug your script.
    if len(arr) > 1:
        middle_point = len(arr) // 2
        left_array = arr[:middle_point]
        right_array = arr[middle_point:]

        # recursion
        merge_sort(left_array)
        merge_sort(right_array)

        # merge
        i = 0   # left arr pointer
        j = 0   # left arr pointer
        merged_array_index = 0

        # compare between the left array and right array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[merged_array_index] = left_array[i]
                i += 1
            else:
                arr[merged_array_index] = right_array[j]
                j += 1
            merged_array_index += 1

        # when right array completed traversing but left array element exists
        while i < len(left_array):
            arr[merged_array_index] = left_array[i]
            i += 1
            merged_array_index += 1

        # when left array completed traversing but right array element exists
        while j < len(right_array):
            arr[merged_array_index] = right_array[j]
            j += 1
            merged_array_index += 1

    return arr


arr_test = [2, 4, 6, 8, 9, 7, 5, 3, 1]

print(merge_sort(arr_test))
