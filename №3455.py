a = int(input('Введите первое целое число от 1 до 1000:\n'))
b = int(input('Введите второе целое число от 1 до 1000:\n'))

hypotenuse = (a ** 2 + b ** 2) ** 0.5

print(round(hypotenuse, 10))