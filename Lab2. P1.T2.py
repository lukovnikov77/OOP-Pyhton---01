import math

class Rational:

    def __init__(self, numerator = 2, denominator = 4):
        reduced_fraction = self.__reduce_fraction(numerator, denominator)
        if reduced_fraction[1] == 0:
            raise ValueError('Denominator cannot be a zero')
        self.__numerator = reduced_fraction[0]
        self.__denominator = reduced_fraction[1]
    
    def __reduce_fraction(self, numerator, denominator):
        k = math.gcd(numerator, denominator)
        return [numerator//k, denominator//k]

    def print_rational(self):
        print(self.__numerator, '/', self.__denominator)

    def print_floating_point_format(self):
        print(self.__numerator / self.__denominator)


rational_number = Rational(4,3)
rational_number.print_rational()
rational_number.print_floating_point_format()