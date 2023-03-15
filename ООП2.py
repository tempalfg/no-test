#Задание 1
#К уже реализованному классу «Дробь» добавьте статический метод, который при вызове возвращает количество созданных объектов класса «Дробь».

#def gcd(m,n):
#
#    while m%n != 0:
#        a = m
#        b = n
#
#        m = b
#        n = a%b
#    return n
#
#class Fraction:
#    __counter = 0
#
#    def __init__(self, numerator,denominator):
#        self.num = numerator
#        self.den = denominator
#        Fraction.__counter += 1
#
#    def __str__(self):
#        return str(self.num) + '/' + str(self.den)
#
#    def __add__(self, other_fraction):
#        new_num = self.num * other_fraction.den + self.den * other_fraction.num
#        new_den = self.den * other_fraction.den
#        common = gcd(new_num,new_den)
#        return  Fraction(new_num//common, new_den//common)
#
#    def __eq__(self, other):
#        first_num = self.num * other.den
#        second_num = other.num * self.den
#        return first_num == second_num
#
#    @staticmethod
#    def get_counter():
#        return Fraction.__counter
#
#
#x = Fraction(3, 4)
#y = Fraction(1, 2)
#print(x + y)
#print(x == y)
#print(Fraction.get_counter())

#Задание 2
#Создайте класс для конвертирования температуры из
#Цельсия в Фаренгейт и наоборот. У класса должно быть
#два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
#класс должен считать количество подсчетов температуры и
#возвращать это значение с помощью статического метода

#class Convert:
#
#    def __init__(self, value):
#        self.val = value
#        Convert.__counter += 1
#
#    @staticmethod
#    def to_fahr(celsius):
#        return 1.8 * celsius + 32
#
#    @staticmethod
#    def to_cels(fahrenheit):
#        return (fahrenheit - 32) / 1.8
#
#print(Convert.to_cels(56))
#print(Convert.to_fahr(4))


