def product_of_add_positions(arr):
    product = 1
    for i in range(1, len(arr), 2):
        product *= arr[i]
    return product

print(product_of_add_positions([1, 2, 3, 4, 5]))