import random
numbers = [0] * 15
for i in range(15):
    numbers[i] = random.randint(1, 100)

print("Элементы массива:")
for num in numbers:
    print(num)