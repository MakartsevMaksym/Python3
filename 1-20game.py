import random

to_be_guessed = random.randint(1,20)
guess = 0
while guess != to_be_guessed:
    try:
        guess = int(input("Введи номер(1-20, 0 - сдаться): "))
        if guess > 0:
            if guess > to_be_guessed:
                print("Слишком много!")
            elif guess < to_be_guessed:
                print("Слишком мало!")
        else:
            print("Сдался.")
            break
    except ValueError:
        print("Введи целое число!")
else:
    print("Угадал!")   
