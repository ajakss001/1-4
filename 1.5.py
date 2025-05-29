def si_v(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.reverse()
    return tuple(unique_numbers)

print(si_v([1, 2, 3, 3, 5]))