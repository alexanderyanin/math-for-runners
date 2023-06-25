print()
normal_text = 'Нормальный ЧСС:'
low_text = 'Нижний ЧСС:'
high_text = 'Верхний ЧСС:'
age = input('Укажите ваш возраст: ')
normal = 220 - int(age)
low = normal * 65 / 100
high = normal * 85 / 100
print()
print(f'{normal_text:20} {normal:10.2f} уд/мин', end='\n\n')
print(f'{low_text:20} {low:10.2f} уд/мин')
print(f'{high_text:20} {high:10.2f} уд/мин')