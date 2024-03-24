from decimal import Decimal
from src.utils.dfp import RoundingMethod
import math

def normalize_significand(significand: str, exponent: str, rounding_method, num_sigfigs=34):
    
    _significand = significand
    _exponent = int(exponent)

    # Extract sign
    sign = 1 if _significand[0] == '-' else 0
    _significand = _significand[1:] if _significand[0] == '+' or _significand[0] == '-' else _significand

    # Remove trailing zeroes
    for i in range(len(significand)):
        index = len(significand) - i - 1
        digit = significand[index]

        if digit != '0':
            break

        if digit.isnumeric():
            _exponent += 1

    # Remove leading zeroes
    _significand = _significand.lstrip('0')

    # Extract the index of the decimal point and the length of string
    decimal_index = _significand.find('.')

    # Extract all digits
    digits = [ ch for ch in _significand if ch.isdigit() ]
    length = len(digits)
    
    # If digits are beyond 34, round off
    if len(digits) > num_sigfigs:
        significant_digits, decimal_point_offset = round_off(
            ''.join(digits), num_sigfigs,
            rounding_method)
        
        _significand = significant_digits 
    else:
        _significand = ''.join(digits)
        _significand =_significand.zfill(num_sigfigs)
    
    if decimal_index != -1:
        _exponent -= (length - decimal_index)
    
    return sign, _significand, str(_exponent)

def round_off(number: str, num_sigfigs, rounding_method: RoundingMethod, sign=0):
    _number = number[:num_sigfigs] + '.' + number[num_sigfigs:num_sigfigs + 2]
    _sign = '-' if sign == 1 else '+'

    print(_sign + _number)
    print(Decimal(_sign + _number))
    
    if rounding_method == RoundingMethod.ROUND_UP:
        print(Decimal(_sign + _number))
        return str(math.ceil(Decimal(_sign + _number))).lstrip('+').lstrip('-'), len(number) - len(number[num_sigfigs:])
    elif rounding_method == RoundingMethod.ROUND_DOWN:
        return str(math.floor(Decimal(_sign + _number))).lstrip('+').lstrip('-'), len(number) - len(number[num_sigfigs:])
    elif rounding_method == RoundingMethod.ROUND_TNE:
        lower_digits = number[num_sigfigs:].rstrip('0')

        place_value = (10 ** (len(lower_digits) - 1))
        midpoint = place_value * 5
        
        print(_sign + number[:num_sigfigs])
        significant_digits = Decimal(_sign + number[:num_sigfigs])
        if int(lower_digits) > midpoint:
            significant_digits += 1
        elif int(lower_digits) < midpoint:
            _number = _number
        else:
            last_significant_digit = Decimal(number[num_sigfigs - 1])
            significant_digits += 1 if last_significant_digit % 2 == 1 else 0

        return str(significant_digits), len(number) - len(number[num_sigfigs:])
