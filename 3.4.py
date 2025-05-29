def find_Largest(a, b):
    return a if a > b else b

num1 = int(input("1 число: "))
num2 = int(input("2 число: "))
print("Наибольшее число: ", find_Largest(num1, num2))