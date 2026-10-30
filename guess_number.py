import random

def guess_the_number():
    # Загадываем случайное число от 0 до 100 включительно
    secret_number = random.randint(0, 100)
    attempts = 0

    print("Я загадал число от 0 до 100. Попробуй угадать!")

    while True:
        try:
            user_input = input("Твой вариант: ")
            guess = int(user_input)
        except ValueError:
            print("Пожалуйста, введи целое число.")
            continue

        attempts += 1

        if guess < 0 or guess > 100:
            print("Число должно быть в диапазоне от 0 до 100.")
        elif guess < secret_number:
            print("Больше!")
        elif guess > secret_number:
            print("Меньше!")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_the_number()
