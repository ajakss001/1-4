def minimum_find(arr):
    if not arr:
        return float('inf')  # Исправлено на 'inf'
    return min(arr)

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
minimum = minimum_find(array)
print("Минимальный элемент массива:", minimum)  # Исправлен текст