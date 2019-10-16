# print('Hello,world')
"""
#Напишите программу, которая спрашивает у пользователя два слова и выводит их разделёнными запятой.

first_word = input('Please enter the first word: ')
second_word = input('Please enter the second word: ')

print(first_word,end=',')
print(second_word)


#Напишите программу, которая запрашивает три целых числа a, b и x и выводит True,
#если x лежит между a и b, иначе – False.

a = int(input('Please enter a: '))
b = int(input('Please enter b: '))
x = int(input('Please enter x: '))
a,b = b,a
if a < x and x < b:
    print(True)
else:
    print(False)


#Напишите программу, которая решает квадратное уравнение ax^2 + bx + c = 0
#Значения a, b и c вводятся с клавиатуры. Для извлечения корня используйте оператор возведения в степень,
#а не функцию math.sqrt, чтобы получить комплексные числа в случае, если подкоренное выражение отрицательно.

a = float(input('Please enter a: '))
b = float(input('Please enter b: '))
c = float(input('Please enter c: '))

D = b**2-4*a*c
#print('D=',D)
if D > 0:
    x1 = (-b+D**1/2.0)/(2*a)
    x2 = (-b-D**1/2.0)/(2*a)
    print("x1=",x1,end=",")
    print("x2=",x2)
elif D == 0:
    x = -b/(2*a)
    print("x= ", x)
else:
    print("There is no root of the equation. Try another numbers, Anton")


#Напишите программу, которая запрашивает у пользователя радиус круга и выводит его площадь.
#Формула площади круга S=pi*R^2 .


import math
R = float(input('Please enter R: '))
pi = math.pi

if R >= 0:
    S = pi*R**2
    print("S=",S)
else:
    print('Вийди, розбійник')


#Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию,
#ввести необходимые числа и получить результат. Операции, которые необходимо реализовать:
#сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.


import math

operator = input('Choose the operator +, -, /, *, ^, sin, cos, tn: ')
if operator == '+' or operator =='-' or operator =='*' or operator =='/':
    a = float(input('Please enter the first number: ').strip())
    b = float(input('Please enter the second number: ').strip())
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        print(a/b)
    else:
        print('0')
elif operator == '^':
    a = float(input('Please enter the number: '))
    n = float(input('Please enter the degree to which to raise the number: '))
    res = pow(a,n)
    print(res)
elif operator == 'sin' or operator =='cos' or operator =='tn':
    a = float(input('Please enter the number: '))
    if operator == 'sin':
        print(math.sin(a))
    elif operator == 'cos':
        print(math.cos(a))
    elif operator == 'tn':
        print(math.tan(a))


#Напишите программу, которая спрашивает у пользователя его имя, 
#и если оно совпадает с вашим, выдаёт определённое сообщение.


My_name = "Anna"
Name = input('Please enter your name: ')

if Name == My_name:
    print('Good boy')
else:
    print('Goodbye')


#Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).


a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
s = 0
if a < b:
    for i in range(a,b+1):
        s = s + i
        i = i + 1
    print(s)
else:
    print("Seems u are an idiot")


#Факториалом числа n называется число 𝑛!=1∙2∙3∙…∙𝑛.
#Создайте программу, которая вычисляет факториал введённого пользователем числа.(цыкл!)

n = int(input('Please enter the n!: '))
fac = 1
for i in range(1,n+1):
    fac = i * fac
    i + 1
print(fac)


#Используя вложенные циклы и функции print(‘*’, end=’’),
# print(‘ ‘, end=’’) и print() выведите на экран прямоугольный треугольник.

height = int(input('Please enter height: '))

for x in range(0,height+1):
        print('*' * x)

#Функция принимает 2 параметра - высоту и ширину прямоугольника. 
#Рисует прямоугольник :)) и возвращает True если был нарисован квадрат и False - если нет.

height = int(input('Please enter height: '))
width= int(input('Please enter width: '))
for x in range(height):
    for y in range(width):
        print('*' ,end='')
    print()
if height == width:
    print(True)
else:
    print(False)

#Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
#Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.


name = input("Enter your name: ")

def hello(name):
    if name:
        print('Hello,',name)
    else:
        print('Hello,Shikaka')
    return name
hello(name)


# Фунция принимает любое число и возвращает суму всех цыфр числа.

num = input('Enter the number: ')


def sum_digit_from_number(num):
    starter = 0
    for i in num:
        starter += int(i)
    return starter


print(sum_digit_from_number(num))



# Пользователь делает вклад в размере N $ сроком на years лет под 11.5% годовых (каждый год размер его вклада увеличивается на 11.5%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя через years лет.

a = int(input('Enter the amount of money: '))
years = int(input('Enter the number of years: '))
stavka = 0.115
z = 0


def bank(a, years):
    for n in range(1, years + 1):
        z = a + a * stavka * n
        n += 1
    return z


print(bank(a, years))

"""
# Написать функцию проверки пароля пользователя при регистрации. Что она должна делать.
# Пользователь вводит два раза пароль(стандартная регистрация)
# Возвращает True , если пользователь ввел два раза пароль верно и есть как минимум 2(заглянуть на функции ord() и chr()) символа с большой буквы. Иначе-False.




user_pass_1 = input('Please, enter the password: ')
user_pass_2 = input('Please, enter the password: ')


def check_password(user_pass_1, user_pass_2):
    if user_pass_1 == user_pass_2:
        FROM_A = ord('A')
        FROM_Z = ord('Z') + 1
        i = 0
        for letter in user_pass_1:
            new_letter = ord(letter)
            if FROM_A <= new_letter <= FROM_Z:
                i += 1
                if i >= 2:
                    return True
    else:
        return False
        
        
print(check_password(user_pass_1, user_pass_2))


"""
# Написать функцию проверки года на высокосный. Возращает True- если высокосний.

year = int(input("Enter the year please: "))


def is_leap(year):
    res = bool()
    if year % 100 == 0:
        if year % 400 == 0:
            res = True
        else:
            res = False
    elif year % 4 == 0:
        res = True
    else:
        res = False
    return res


print(is_leap(year))
"""