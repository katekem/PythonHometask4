# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
size = int(input('Введите max степень: '))
koef = {}
for i in range(size+1):
    koef[i] = random.randint(0,100)
print(koef)

equation = ''
for i in range(size, -1, -1):
    if koef[i] != 0:
        equation += f'{koef[i]}*x**{i} + '
    elif koef[i] == 1:
        equation += f'{koef[i]}*x + '
    elif i == 0:
        equation +=f'{koef[i]}' 
    else:
        equation += f''
print(equation)