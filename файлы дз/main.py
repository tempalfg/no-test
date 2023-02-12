#Задание 1
#Дано два текстовых файла. Выяснить, совпадают ли
#их строки. Если нет, то вывести несовпадающую строку
#из каждого файла
#f = open(file='text1', mode='r', encoding='UTF-8')
#lines = set(f.read().split())
#f.close()
#print('Первое множество:', lines)
#f = open(file='text2', mode='r', encoding='UTF-8')
#lines2 = set(f.read().split())
#f.close()
#print('Второе множество:', lines2)
#
#intersection = lines.intersection(lines2)
#if len(intersection) > 0:
#    print('Совпадения: ', intersection)
#else:
#    print('Совпадения нет')

#Задание 3
#Дан текстовый файл. Удалить из него последнюю
#строку. Результат записать в другой файл
#with open(file='text1', mode='r', encoding='UTF-8') as f:
#    line = f.readlines()
#    line = line[:1]
#
#with open(file='text1', mode='w',encoding='UTF-8') as f:
#    f.writelines(line)

#Задание 2
#Дан текстовый файл. Необходимо создать новый файл
#и записать в него следующую статистику по исходному
#файлу:
#■ Количество символов;
#■ Количество строк;
#■ Количество гласных букв;
#■ Количество согласных букв;
#■ Количество цифр.
#with open(file='text1', mode='r', encoding='UTF-8') as f:
#    count = 0
#    for i in f:
#        count += len(i) - 1
#    count += 1
#    print('Количество символов: ', count)
#
#print('Количество строк: ', sum(1 for line in open('text1', mode='r')))
#
#with open(file='text1', mode='r', encoding='UTF-8') as f:
#    vowels = 'eyuioa'
#    count = 0
#    for i in f.read():
#        if i in vowels:
#            count += 1
#    print('Количество гласных: ' , count)
#
#with open(file='text1', mode='r', encoding='UTF-8') as f:
#    consonants = 'bcdfghjklmnpqrstvwxyz'
#    count = 0
#    for i in f.read():
#        if i in consonants:
#            count += 1
#    print('Количество согласных: ', count)
#
#with open(file='text1', mode='r', encoding='UTF-8') as f:
#    num = '0123456789'
#    count = 0
#    for i in f.read():
#        if i in num:
#            count += 1
#    print('Количество цифр: ', count)
#
#
#with open(file='text3', mode='w+', encoding='UTF-8') as f:
#    f.write('Количество символов:12\nКоличество строк:3\nКоличество гласных:4\nКоличество согласных:6\nКоличество цифр: 2')

#Задание 4
#Дан текстовый файл. Найти длину самой длинной
#строки.
#with open(file='slowo', mode='r', encoding='UTF-8') as f:
#    print(len(max(f.readlines())))







