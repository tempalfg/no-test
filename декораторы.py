#Создайте декоратор для повторной попытки выполнения функции с определенным количеством попыток в случае сбоя
#import random
#
#
#def retry(num):
#    def decorator(func):
#        def wrapper(*args):
#            for i in range(num):
#                try:
#                    return func(*args)
#                except Exception:
#                    if i == num:
#                        raise Exception ('Слишком много попыток вызова')
#        return wrapper
#    return decorator
#
#"@retry(num=3)
#def get_one():
#    print('Вызов функции...')
#    if random.randint(0,1):
#        raise ValueError('Функция не сработала!')
#    return 'Фунция успешно сработала!'
#
#print(get_one())