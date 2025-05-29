import random

length = random.randint(5, 25)
start = random.randint(50, 200) * 3
arr = [start - 3*i for i in range(length)]
print(arr)