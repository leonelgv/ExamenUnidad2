"""
>>> circulo = Circulo(2)
>>> circulo.getArea()
12.566370614359172
"""

import math

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, radio):
        if(radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        return 0

    def calcularPerimetro(self):
        return 0

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

if __name__==  '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")