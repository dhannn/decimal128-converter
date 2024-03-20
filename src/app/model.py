from src.utils.dfp import *


class MockDecimalFloatingPoint(DecimalFloatingPoint):

    def __str__(self) -> str:
        return '0 11011 100100001010011101001 0001010011 1001001001 1011010111 1101011101 0101011011 0110100011 1010110110 0101011011'

    def to_hex(self) -> str:
        return '0372 14E9 14E4 9B5F 5D56 DA3A D95B'

    def __init__(self):
        pass

""" TODO: Implement conversion to decimal

Should take a float value (precondition is any string version is type
casted by the controller class), convert it by using the DecimalFloatingPoint
class and return the object

Should raise a NaNException when not a number
"""
def convert_to_decimal(value: float, method: RoundingMethod) -> DecimalFloatingPoint:
    return MockDecimalFloatingPoint()

""" TODO: Implement saving to text file functionality

Should take the user input and the output, and save it 

Follow the following format
Base-10 value:              [original_value]
Decimal128 representation:  [str(decimal)] 
                            [decimal.to_hex()]
"""
def save_to_text_file(
        original_value: float, 
        decimal: DecimalFloatingPoint, 
        ) -> None:
    pass
