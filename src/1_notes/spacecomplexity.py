

# arr is [1, 2, ... 10]
def baz(arr):
    evens = []

    # we're adding half of the values from the input array

    for n in arr:
        if n % 2 == 0:
            evens.append(n)  # 0(n/2)== 0(1/2 * n)
    return evens
