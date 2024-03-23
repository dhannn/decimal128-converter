import math
from src.utils.dfp import *


class MockDecimalFloatingPoint(DecimalFloatingPoint):

    def set_vars(self, significand, exponent):
        self.significand = significand
        self.exponent = exponent

        return self

    def __str__(self) -> str:
        if math.isnan(self.exponent) or math.isnan(self.significand == float('NaN')):
            return 'NaN representation'

        return '0 11011 100100001010011101001 0001010011 1001001001 1011010111 1101011101 0101011011 0110100011 1010110110 0101011011'

    def to_hex(self) -> str:
        if math.isnan(self.exponent) or math.isnan(self.significand == float('NaN')):
            return 'NaN representation'
        
        return '0372 14E9 14E4 9B5F 5D56 DA3A D95B'

    def __init__(self):
        pass


class Model:

    significand: float
    exponent: int
    roundingOption: RoundingMethod
    
    def set_vars(self, signifcand: str, exponent: str, roundingOption: RoundingMethod):
        self.significand = signifcand
        self.exponent = exponent
        self.roundingOption = roundingOption

    def convert_to_decimal(self) -> DecimalFloatingPoint:
        # if math.isnan(self.exponent) or math.isnan(self.significand == float('NaN')):
        #     return NaNDecimalFloatingPoint()

        return DecimalFloatingPoint(self.significand, self.exponent, self.roundingOption)
        # return MockDecimalFloatingPoint().set_vars(self.significand, self.exponent)
    
    def save_to_text_file(self) -> None:
        dfp: DecimalFloatingPoint
        dfp = self.convert_to_decimal()
        
        bin_dfp = str(dfp)
        hex_dfp = dfp.to_hex()

        with open(f'Decimal128_{ dfp.significand }e{ dfp.exponent }.txt', 'w') as file:
            file.write(f'Base-10:\t\t{ dfp.significand }e{ dfp.exponent }\nDecimal128:\t\t{bin_dfp} (binary)\n\t\t\t\t{hex_dfp} (hex)')
