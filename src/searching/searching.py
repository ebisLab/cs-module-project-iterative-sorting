position = -1


def linear_search(arr, target):
    # Your code here

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # i thought -1 was also false


# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            globals()['position'] = i
            return i
        i = i + 1

    # for i in range(len(arr)):
    #     # Your code here
    #     if arr[i] == target:
    #         return i

    return -1  # not found
