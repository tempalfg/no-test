#Пользователь вводит с клавиатуры строку. Проверьте
#является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
#слева направо и справа налево. Например, кок; А роза
#упала на лапу Азора; доход; А буду я у дуба
#a = input('Введите выражение: ')
#if a != a[::-1]:
#    print('Это  не палиндром ')
#else:
#    print('Это палиндром')

#mytext = "Выдали даме на станции четыре зелёных квитанции о том, что получен багаж: диван, чемодан, Саквояж, картина, корзина, картонка и маленькая собачонка. Вещи везут на перрон. Кидают в открытый вагон. Готово. Уложен багаж: Диван, чемодан, саквояж, картина, корзина, картонка и маленькая собачонка."
#mytext_temp = mytext.lower()
#listold = list(mytext.split())
#listnew = list(mytext_temp.split())
#word = ["диван","чемодан","саквояж","картина","корзина","картонка","маленькая","собачонка"]
#for i in range(len(listnew)) :
#    for j in word :
#        if j in listnew[i] :
#            listold[i] = listnew[i].upper()
#print(' '.join(listold))

#a = input('Введите математическое выражание: ')
#
#if '+' in a:
#    oper = a.index('+')
#    print(int(a[:oper]) + int(a[oper + 1::]))

#Задание 1:
#Пользователь вводит с клавиатуры арифметическое
#выражение. Например, 23+12.
#Необходимо вывести на экран результат выражения.
#В нашем примере это 35. Арифметическое выражение
#может состоять только из трёх частей: число, операция,
#число. Возможные операции: +, -,*,/
#a = input('Введите математическое выражение: ')
#print(eval(a))                                        # :)

#Задание 2:
#В списке целых, заполненном случайными числами,
#определить минимальный и максимальный элементы,
#посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
#количество нулей. Результаты вывести на экран.

#import random
#result = [random.randrange(-1000,2000) for i in range(10)]
#print ('Случайный список чисел: '+ str(result))
#a = max(result)
#print('Макс. число: ', a)
#b = min(result)
#print('Мин. число: ', b)
#print('Кол-во положительных чисел:', sum(i > 0 for i in result))
#print('Кол-во отрицательных чисел:', sum(i < 0 for i in result))