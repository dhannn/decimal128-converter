from utils.dfp import *


class NaNException(Exception): pass

""" Implement conversion to decimal

Should take a float value (precondition is any string version is type
casted by the controller class), convert it by using the DecimalFloatingPoint
class and return the object

Should raise a NaNException when not a number
"""
def convert_to_decimal(value: float, method: RoundingMethod) -> DecimalFloatingPoint:
    pass

""" Implement saving to text file functionality

Should take the user input and the output, and save it 

Follow the following format
Base-10 value:              [original_value]
Decimal128 representation:  [str(decimal)] 
                            [decimal.to_hex()]
"""
def save_to_text_file(
        original_value: float, 
        decimal: DecimalFloatingPoint, 
        filename: str) -> None:
    pass
