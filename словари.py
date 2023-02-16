#Задание 1
#Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
#его рост. Требуется реализовать возможность добавления,
#удаления, поиска, замены данных. Используйте словарь
#для хранения информации.

#players = {'Karry': {'name': 'Stephen', 'height': 178},'Lebron': {'name': 'James', 'height': 202},'Jordan': {'name': 'Michael','height': 212 }}
#command = input('Введите команду (add/delete/find/replace)')
#
#while   True:
#    if command == 'add' or command == 'replace':
#        name = input('Введите имя: ')
#        surname = input('Введите фамилию: ')
#        height = input('Введите рост: ')
#        players[height] = height
#        players[name] = surname
#        if command == 'add':
#            print('Имя,фамилия, рост добавлены успешно')
#        else:
#            print('Имя,фамилия,рост изменены успешно')
#
#    elif command == 'delete':
#        name = input('Введите имя, которое вы хотите удалить: ')
#        surname = input('Введите фамилию, которую хотите удалить: ')
#        height = input('Введите рост, который хотите удалить: ')
#        if surname and name and height in players:
#            del players[name]
#            del players[height]
#            del players[surname]
#            print('Имя,фамилия,рост удалены успешно')
#        else:
#            print('Ошибка')
#    elif command == 'find':
#        name = input('Введите имя ,которое хотите найти: ')
#        surname = input('Введите фамилию, которую хотите найти')
#        height = input('Введит рост для поиска: ')
#        print(f'Имя: {name}, Фамилия: {surname}, Рост: {height}')

#Задание 3
#Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
#название должности, номер кабинета, skype. Требуется
#реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
#информации

firma = {'Artem': {'surname': 'Parsadanyan', 'job_title': 'accountant', 'number': 7892317143, 'email': 'tempa@gmail.com', 'number_room': 12 },
        'Igor': {'surname': 'Smolyaninov', 'job_title': 'cashier', 'number': 7892647282, 'email': 'smola@gmail.com', 'number_room': 1},
        'Kiril': {'surname': 'Paymushin', 'job_title': 'cleaner', 'number': 7892892742, 'email': 'kxxr@yandex.ru', 'number_room': 22}}


while True:
    command = input('Введите команду: (add/delete/find/replace)')
    if command == 'add' or command == 'replace':
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        job_title = input('Введите должность: ')
        number_room = input('Введите номер кабинета: ')
        firma[name] = name
        firma[surname] = surname
        firma[job_title] = job_title
        firma[number_room] = number_room
        if command == 'add':
            print('Новые данные добавлены успешно!')
        else:
            print('Замены проведены успешно!')                                        #так и не работают программы find и replace, add и delete работают

    elif command == 'delete':
        name = input('Введите имя для удаления: ')
        surname = input('Введите фамилию для удаления: ')
        job_title = input('Введите должность для удаления: ')
        number_room = input('Введите номер кабинета для удаления: ')
        if name and surname and job_title and number_room in firma:
            del[name]
            del[surname]
            del[job_title]
            del[number_room]
        print('Удаление успешно!')

    elif command == 'find':
        name = input('Введите имя ,которое хотите найти: ')
        surname = input('Введите фамилию ,которую хотите найти: ')
        job_title = input('Введите должность ,которую хотите найти: ')
        number_room = input('Введите номер кабинета ,которую хотите найти: ')
        print(f'Имя: {name}, Фамилия: {surname}, Должность: {job_title}, Номер кабинета: {number_room}')