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