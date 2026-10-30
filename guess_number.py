import random

def guess_the_number():
    while True:
        secret_number = random.randint(0, 100)
        attempts = 0

        print("\nЯ загадал число от 0 до 100. Попробуй угадать!")

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

        # После победы спрашиваем, хочет ли пользователь продолжить
        while True:
            choice = input("Хочешь сыграть ещё раз? (да/нет): ").strip().lower()
            if choice in ["да", "д", "yes", "y"]:
                break  # выход из внутреннего цикла выбора, игра начнётся заново
            elif choice in ["нет", "н", "no", "n"]:
                print("Спасибо за игру! До встречи!")
                return  # завершаем функцию, программа закончится
            else:
                print("Пожалуйста, ответь «да» или «нет».")

if __name__ == "__main__":
    guess_the_number()
