
#Задание 1
#Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 без
#остатка) нужно вывести слово Fizz. Если число кратно 5
#нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
#вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
#вывести само число.
#Если пользователь ввел значение не в диапазоне от 1
#до 100 требуется вывести сообщение об ошибке.

#a = int(input("Введите число от 1 до 100: "))
#if a % 15 == 0 and a % 5 == 0:
#    print("Fizz Buzz")
#elif a % 5 == 0:
#    print("Buzz")
#elif a % 3 == 0:
#    print("Fizz")
#elif a % 3 != 0 and a % 5 != 0:
#    print(a)
#else:
#    print("Ошибка, требуется ввести число от 1 до 100")

#Написать программу, которая по выбору пользователя возводит введенное им число в степень от нулевой
#до седьмой включительно
#a = int(input("Введите число: "))
#select = int(input("Выберите степень в которую хотите возвести указанное вами число 0-7: " ))
#if select == 0:
#    degree = a ** 0
#    print(degree)
#elif select == 1:
#    degree = a ** 1
#    print(degree)
#elif select == 2:
#    degree = a ** 2
#    print(degree)
#elif select == 3:
#    degree = a ** 3
#    print(degree)
#elif select == 4:
#    degree = a ** 4
#    print(degree)
#elif select == 5:
#    degree = a ** 5
#    print(degree)
#elif select == 6:
#    degree = a ** 6
#    print(degree)
#elif select == 7:
#    degree = a ** 7
#    print(degree)
#else:
#    print("Ошибка")

price = int(input('Введите стоимость звонка: '))
operator = int(input('Выберите с какого на какой оператор хотите позвонить: 1-Теле2, МТС '
                     '2-МТС, Мотив '
                     '3-Теле2, Мотив'))