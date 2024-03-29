from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from src.utils.RoundingMethod import RoundingMethod

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
    
    # Restore exponent if all zeroes
    if len(_significand) == _exponent - Decimal(exponent):
        _exponent = Decimal(exponent)

    # Remove leading zeroes
    _significand = _significand.lstrip('0')

    # Extract the index of the decimal point and the length of string
    decimal_index = _significand.find('.')

    # Extract all digits
    digits = [ ch for ch in _significand if ch.isdigit() ]
    length = len(digits)

    if decimal_index == -1:
        decimal_index = length
    
    # If digits are beyond 34, round off
    if len(digits) > num_sigfigs:
        significant_digits, _ = round_off(
            ''.join(digits), num_sigfigs,
            rounding_method)
        
        _significand = significant_digits
        _exponent += (decimal_index - num_sigfigs)
    else:
        _significand = ''.join(digits)
        _significand = _significand.zfill(num_sigfigs)
        _exponent -= (length - decimal_index)
    
    
    return sign, _significand, str(_exponent)

def round_off(number: str, num_sigfigs, rounding_method: RoundingMethod, sign=0):
    _number = number[:num_sigfigs] + '.' + number[num_sigfigs:num_sigfigs + 2]
    _sign = '-' if sign == 1 else '+'
    
    dec = Decimal(_sign + _number) 
    print(str(dec.to_integral_exact(ROUND_FLOOR)).lstrip('+').lstrip('-'))
    if rounding_method == RoundingMethod.ROUND_UP:
        return str(dec.to_integral_exact(ROUND_CEILING)).lstrip('+').lstrip('-'), len(number) - len(number[num_sigfigs:])
    elif rounding_method == RoundingMethod.ROUND_DOWN:
        print(str(dec.to_integral_exact(ROUND_CEILING)).lstrip('+').lstrip('-'))
        return str(dec.to_integral_exact(ROUND_FLOOR)).lstrip('+').lstrip('-'), len(number) - len(number[num_sigfigs:])
    elif rounding_method == RoundingMethod.ROUND_TNE:
        return str(dec.to_integral_exact(ROUND_HALF_EVEN)).lstrip('+').lstrip('-'), len(number) - len(number[num_sigfigs:])
