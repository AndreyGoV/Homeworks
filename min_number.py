first_num = int(input('Введите первое число: \n')) # 5
second_num = int(input('Введите второе число: \n')) # 6
third_num = int(input('Введите третье число: \n')) # 4
fourth_num = int(input('Введите четвёртое число: \n')) # 8
fifth_num = int(input('Введите пятое число: \n')) # 7

if first_num < second_num and first_num < third_num and first_num < fourth_num and first_num < fifth_num:
    print(f'Наименьшее число:\n{first_num}')
elif second_num < third_num and second_num < fourth_num and second_num < fifth_num:
    print(f'Наименьшее число:\n{second_num}')
elif third_num < fourth_num and third_num < fifth_num:
    print(f'Наименьшее число:\n{third_num}')
elif fourth_num < fifth_num:
    print(f'Наименьшее число:\n{fourth_num}')
else:
    print(f'Наименьшее число:\n{fifth_num}')