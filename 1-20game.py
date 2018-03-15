import random

def guess_number():
	secretNumber = random.randint(1,20)
	print('Угадай число от 1 до 20.')
	acc = 0
	while True:
		try:
			number = int(input('Введите число: '))
			acc += 1
			if number < secretNumber:
				print('Больше!')
			elif number > secretNumber:
				print('Меньше!')
			else:
				print('\n		Победа!')
				print('\n	Число, яке Вы ввели ' + str(number), sep='')
				break
		except ValueError:
			print('Неверный ввод.')
			continue
	return acc
times = guess_number()
print('    Вы угадали число с ' + str(times) + ' попытки')
