print()
age = input('Укажите ваш возраст: ')
normal = 220 - int(age)
low = normal * 65 / 100
high = normal * 85 / 100
print()
print('Нормальный ЧСС: ', normal, 'уд/мин', end='\n\n')
print('Нижний ЧСС: ', low, 'уд/мин')
print('Верхний ЧСС: ', high, 'уд/мин')

