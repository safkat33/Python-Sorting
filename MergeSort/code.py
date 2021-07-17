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
        left_array_pointer = 0
        right_array_pointer = 0
        merged_array_index = 0
        while left_array_pointer < len(left_array) and right_array_pointer < len(right_array):
            if left_array[left_array_pointer] < right_array[right_array_pointer]:
                arr[merged_array_index] = left_array[left_array_pointer]
                left_array_pointer += 1
            else:
                arr[merged_array_index] = right_array[right_array_pointer]
                right_array_pointer += 1
            merged_array_index += 1

        while left_array_pointer < len(left_array):
            arr[merged_array_index] = left_array[left_array_pointer]
            left_array_pointer += 1
            merged_array_index += 1

        while right_array_pointer < len(right_array):
            arr[merged_array_index] = right_array[right_array_pointer]
            right_array_pointer += 1
            merged_array_index += 1

    return arr


arr_test = [2, 4, 6, 8, 9, 7, 5, 3, 1]

print(merge_sort(arr_test))
