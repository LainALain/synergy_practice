import math


def calculate_factorial(n):
    try:
        n = int(n)
    except ValueError:
        return "Ошибка: введите целое число."

    if n <= 0:
        return "Ошибка: число должно быть положительным."

    return math.factorial(n)


while True:
    user_num = input("Введите положительное целое число >>> ").strip()
    result = calculate_factorial(user_num)

    if isinstance(result, int):
        print(f"Факториал числа {user_num} равен {result}")
        break
    else:
        print(result)
