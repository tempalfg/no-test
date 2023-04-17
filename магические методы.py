#class Complex:
#
#    def __init__(self,real,imag):
#        self.real = real
#        self.imag = imag
#
#    def __add__(self, other):
#        return Complex(self.real + other.real, self.imag + other.real)
#
#    def __sub__(self, other):
#        return Complex(self.real - other.real, self.imag - other.real)
#
#    def __mul__(self, other):
#        return Complex(self.real * other.real - (self.imag * other.imag), self.imag * other.real + other.imag * self.real)
#
#    def __truediv__(self, other):
#        pass
#
#    def __lt__(self, other):
#        return self.real + self.imag > other.real + other.imag
#
#    def __le__(self, other):
#        return self.real + self.imag >= other.real + other.imag
#
#    def __gt__(self, other):
#        return self.real + self.imag > other.real + other.imag
#
#    def __ge__(self, other):
#        return self.real + self.imag >= other.real + other.imag
#
#    def __eq__(self, other):
#        return self.real == other.real and self.imag == other.imag
#
#    def __iadd__(self, other):
#        return self.__add__(other)
#
#    def __str__(self):
#        return f'{self.real} + {self.imag}i'
#
#a = Complex(5,2)
#b = Complex(3,7)
#print(a,b)
#print(a + b)
#print(a * b)
#a += b
#print(a)

#class Circle:
#    def __init__(self, radius: int):
#        self.radius = radius
#
#    def circ_len(self):  # длина окружности
#        return self.radius * 3.14 * 2
#
#    def __eq__(self, other):  # ==
#        return self.radius == other.radius
#
#    def __lt__(self, other):  # <
#        return self.circ_len() < other.circ_len()
#
#    def __le__(self, other):  # <=
#        return self.circ_len() <= other.circ_len()
#
#    def __gt__(self, other):  # >
#        return self.circ_len() > other.circ_len()
#
#    def __ge__(self, other):  # >=
#        return self.circ_len() >= other.circ_len()
#
#    def __add__(self, num: int):  # +
#        return Circle(self.radius + num)
#
#    def __iadd__(self, num: int):  # +=
#        self.radius += num
#
#    def __sub__(self, num: int):  # +
#        return Circle(self.radius + num)
#
#    def __isub__(self, num: int):  # +
#        return self.__sub__(other)
#
#a = Circle(2)
#print(a)