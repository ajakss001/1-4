def count_squares(width, height, square_size):
    return (width // square_size) * (height // square_size)

w = int(input("Ширина прямоугольника: "))
h = int(input("Высота прямоугольника: "))
s = int(input("Сторона квадрата: "))
print("Количество квадратов:", count_squares(w, h, s))