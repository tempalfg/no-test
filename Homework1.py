# Задание 1
# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат
# вычислений вывести на экран.
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
a = (number1 + number2 + number3)
print(a)
b = (number1 * number2 * number3)
print(b)

#Задание 2
#Пользователь вводит с клавиатуры три числа. Первое
#число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, третье число — задолженность за коммунальные услуги. Необходимо вывести
#на экран сумму, которая останется у пользователя после
#всех выплат.
num1 = int(input("Введите вашу ЗП: "))
num2 = int(input("Введите сумма ежм.платежа в банке: "))
num3 = int(input("Введите долг за ком.усл: "))
remainder = (num1 - (num2 + num3))
print("Ваш остаток", remainder, "руб.")

#Задание 3
#Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его
#диагоналей.
a = int(input("Введите длину первой диагонали: "))
b = int(input("Введите длину второй диагонали: "))
area_rhombus = (a * b / 2)
print("Площадь ромба", area_rhombus)

#Задание 4
#Выведите на экран надпись To be or not to be на разных
#строках. Пример вывода:
#To be
#or not
#to be
print("To be\nor not\nto be")

#Задание 5
#Выведите на экран надпись «Life is what happens when
#you're busy making other plans» John Lennon на разных
#строках. Пример вывода:
print('''“Life is what happens
               when
                   you’re busy making other plans” John Lennon.''')

#Задание 1
#Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры. Например,
#если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.
number_1 = input("Введите первое число: ")
number_2 = input("Введите второе число: ")
number_3 = input("Введите третье число: ")
total = (number_1 + number_2 + number_3)
print(total)

#Задание 2
#Пользователь вводит с клавиатуры число, состоящее
#из четырех цифр. Требуется найти произведение цифр.
#Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.
a = int(input("Введите четырехзначное число: "))
a4, a = a % 10, a//10
a3, a = a % 10, a//10
a2, a = a % 10, a//10
print(a4 * a3 * a2 * a)
#Задание 3
#Пользователь вводит с клавиатуры количество метров.
#Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили.
meters = int(input("Введите метры: "))
centimeters = (meters * 100)
print(centimeters, "сантиметров")
decimeters = (meters * 10)
print(decimeters, "дециметр/ов")
millimeters = (meters * 1000)
print(millimeters, "миллиметров")
miles = (meters * 0.000621371)
print(miles, "миль")

#Задание 4
#Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер
#основания треугольника и размер высоты.
a = int(input("Введите основание треугольника: "))
b = int(input("Введите высоту треугольника: "))
square_triangle = (a * b / 2)
print(square_triangle, "площадь треугольника")

#Задание 5
#Пользователь с клавиатуры вводит четырёхзначное
#число. Необходимо перевернуть число и отобразить
#результат. Например, если введено 4512, результат 2154.
a = int(input("Введите четырехзначное число: "))
a4, a = a % 10, a//10
a3, a = a % 10, a//10
a2, a = a % 10, a//10
print(a4 * 1000 + a3 * 100 + a2 * 10 + a)