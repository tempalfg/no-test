import numpy

#numbers_list = [1, 23, 43, 16 , 12, 75]
#b = numbers_list[:4]
#c = numbers_list[:3]
#x = numbers_list[4:]
#
#print(numpy .mean(b), 'среднее арифметическое')
#if numpy. mean(numbers_list) > 0:
#    b.sort()
#    print(b)
#elif numpy. mean(numbers_list) < 0:
#    c.sort()
#    print(c)
#print(x[::-1])

#Задание 2
#Написать программу «успеваемость». Пользователь
#вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
#меню для пользователя:
#■ Вывод оценок (вывод содержимого списка);
#■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
#■ Выходит ли стипендия (стипендия выходит, если
#средний бал не ниже 10.7);
#■ Вывод отсортированного списка оценок: по возрастанию или убыванию.

#estimates = list(map(int, input('Введите числа от 1 до 12 через запятую: ').split(',')))
#
#
#while True:
#    command = input('Введите команду: Вывод оценок/Пересдача экзамена/Выходит ли стипендия/Вывод отсортированного списка оценок: по возрастанию или убыванию')
#
#    if command == 'Вывод оценок':
#        print('оценки', estimates)
#    elif command == 'Пересдача экзамена':
#        number = int(input('Введите номер элемента списка: '))
#        new_estimates = int(input('Введите новую оценку: '))
#        estimates[number] = new_estimates
#        print(estimates)
#    elif command == 'Выходит ли стипендия':
#        if numpy. mean (estimates) >= 10.7:
#            print('Степендия выходит')
#        else:
#            print('Степендия не выходит')
#    elif command == 'Вывод отсортированного списка оценок: по возрастанию или убыванию':
#        a = sorted(estimates)
#        print(a, 'по возрастанию')
#        estimates.sort(reverse=True)
#        print(estimates, 'по убыванию')



