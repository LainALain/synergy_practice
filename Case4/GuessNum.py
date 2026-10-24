import random 

counter = 0
Num = random.randint(1, 100)

while counter < 5:
    user_guess = input("Угадайте число от 1 до 100 >>> ").strip()

    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Ошибка: введите целое число.")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Ошибка: число должно быть в диапазоне от 1 до 100.")
        continue

    counter += 1

    if user_guess < Num:
        print("Слишком мало!")
    elif user_guess > Num:
        print("Слишком много!")
    else:
        print(f"Поздравляем! Вы угадали число {Num} за {counter} попыток.")
        break