# add_contact(name, phone_number) -> None (Добавляет контакт в книгу)
# remove_contact(name) -> None (Удаляет контакт если он был, иначе
# выводит сообщение об ошибке)

# update_contact(name, phone_number) -> None (Изменяет номер
# телефона у контакта с именем name)

# get_contact(name) -> str(phone_number) (Возвращает номер телефона по имени)
# get_all_contacts() -> list (Возвращает список всех записей)

#class Phonebook:
#    def __init__(self):
#        self.components = {}
#
#    def add_contact(self, name, phone_number):
#        self.components[name] = phone_number
#
#    def remove_contact(self, name):
#        if name in self.components:
#            del self.components[name]
#            print('Контакт удален')
#        else:
#            print('Такого контакта нет')
#
#
#    def update_contact(self, name):
#        new_number = int(input('Введите номер телефона: '))
#        self.components[name] = new_number
#        print('Контакт обновлен')
#
#    def get_contact(self, name):
#        return self.components[name]
#
#    def get_all_contacts(self):
#        list_comp = []
#        for key, value in self.components.items():
#            list_comp.append([key, value])
#        return list_comp
#
#my_phone = Phonebook()
#my_phone.add_contact('Artem', '+92328132')
#print(my_phone.get_all_contacts())
#print(my_phone.get_contact('Artem'))
#my_phone.update_contact('Artem')
#print(my_phone.get_all_contacts())
#my_phone.remove_contact('Artem')
#my_phone.remove_contact('Artem')

# 2.

#import time


#class Timer:
#    pass

# Реализуйте класс Timer, поддерживающий следующие методы:
#
# start(): запускает таймер
# stop(): останавливает таймер
# reset(): сбрасывает таймер на ноль
# elapsed_time(): возвращает время, прошедшее с
# момента запуска таймера, в секундах

#import time
#
#class Timer:
#    def __init__(self):
#        self.start_time = None
#        self.time = 0
#
#    def format_time(self, time):
#        return round(time, 3)
#
#    def start(self):
#        if self.start_time is None:
#            self.start_time = time.time()
#        else:
#            print('Таймер уже запущен')
#
#    def stop(self):
#        if self.start_time is not None:
#            self.time = self.format_time(time.time() - self.start_time)
#        else:
#            print('Таймер не был запущен')
#
#    def reset(self):
#        self.start_time = None
#
#    def elapsed_time(self):
#        if self.start_time:
#            return self.format_time(time.time() - self.start_time)
#        return 'Таймер не был запущен'
#
#
#timer = Timer()
#timer.start()
#[i for i in range(100000)]
#timer.stop()
#print(timer.time)
#print(timer.elapsed_time())





