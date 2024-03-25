from bitarray import bitarray
from enum import Enum
from src.utils.bcd import BCD
from src.utils.dpd import DPD
from decimal import Decimal


class RoundingMethod(Enum):
    ROUND_UP = 0
    ROUND_DOWN = 1
    ROUND_TNE = 3

class DecimalFloatingPoint:
    
    BIAS: int = 6176

    significand: float
    exponent: int
    rounding_method: RoundingMethod
    __exponent_representation: int                      # this is with bias
    __sign: str                                         # only '+' or '-'
    __combination_field: bitarray                       # should be five bits
    __exponent_continuation_field: bitarray             # should be twelve bits

    # should be list of four three-bit bitarrays (densely-packed)
    __coefficient_continuation_field: list[bitarray]   
    # bitarray of 128 bits combining everything
    decimal_value: bitarray
    
    """ TODO: Implement the constructor

    Should take in a numeric type or a string equivalent of the float and
    call the __get_combination_field, __get_exponent_continuation_field and
    __get_coefficient_continuation_field to populate the object variables

    Decimal value is all the parts combined in one bitarray
    """
    def __init__(self, significand: str, exponent: str, rounding_method):
        # To handle positive and negative zeroes
        if Decimal(significand) == 0 or Decimal(significand) == -0 or Decimal(exponent) < -6176:
            if significand[0] == '-':
                self.decimal_value = bitarray('1')
            else:
                self.decimal_value = bitarray('0')
            self.decimal_value.extend('010 0010 0000 1000')
            self.decimal_value.extend('0' * 112)
        
        # To handle positive and negative infinity
        elif Decimal(exponent) >= 6112:   
            if significand[0] == '-':
                self.decimal_value = bitarray('1')
            else:
                self.decimal_value = bitarray('0')
            self.decimal_value.extend('111 1000')
            self.decimal_value.extend('0' * 120)   

        else:
            def normalize_significand(significand: str, exponent):
                # Remove trailing zeroes
                for i in range(len(significand)):
                    index = len(significand) - i - 1
                    digit = significand[index]

                    if digit != '0':
                        break

                    if digit.isnumeric():
                        exponent += 1

                # Remove padded zeroes
                if not(significand[0] == '-' or significand[0] == '+'):         # If significand has no sign
                    significand = significand.lstrip('0')
                else:                                                           # If first char is a sign
                    significand = significand[0] + significand[1:].lstrip('0')

                # If significand contains a decimal point 

                index_decimal_point = significand.find(".")     # Store index of decimal point
                
                digits = [ch for ch in significand if ch.isdigit()]
                length = len(digits)
                normalized_str = ''
                if length > 34:
                    significand = ''.join(digits[:34])
                    lower_digits = ''.join(digits[34:])

                    significand = round_off(significand, lower_digits, rounding_method)
                    normalized_str = significand + '.' + lower_digits
                else:   
                    significand = ''.join(digits[:length]) # Move decimal point to the rightmost part
                    normalized_str = significand + '.'     # Appends decimal point to end 

                
                significand = significand.zfill(34)
                new_index_decimal_point = normalized_str.find(".")  # Find new position of decimal point

                if index_decimal_point != -1:
                    exponent = int(exponent)
                    exponent += (index_decimal_point - new_index_decimal_point)

                return significand, exponent

            # assume significand is a string where integer part is already 34 digits and decimal point is appropriately set
            def round_off(significand, lower_digits, rounding_method) -> str:
                significand_dec = int(significand)

                place_value = (10 ** (len(lower_digits) - 1))
                midpoint = place_value * 5

                if rounding_method == RoundingMethod.ROUND_UP:
                    return str(significand_dec + 1)
                elif rounding_method == RoundingMethod.ROUND_DOWN:
                    return significand
                elif rounding_method == RoundingMethod.ROUND_TNE:
                    if int(lower_digits) == midpoint:          
                        if significand_dec % 2 == 0:    
                            return significand
                        else:
                            return str(significand_dec + 1)
                    elif int(lower_digits) > midpoint:                               
                        return str(significand_dec + 1)
                    elif int(lower_digits) < midpoint:   
                        return significand

            if significand[0] == '-':
                significand = significand[1:]
                self.__sign = 1
            else:
                self.__sign = 0

            significand, exponent = normalize_significand(significand, exponent)
            
            self.significand = significand
            self.exponent = int(exponent)
            self.rounding_method = rounding_method
            
            # Setting the sign
            # Setting the combination field
            self.__combination_field = self.__get_combination_field(self.significand, self.exponent)
            # Setting the exponent continuation field
            self.__exponent_continuation_field = self.__get_exponent_continuation_field(self.exponent)
            # Setting the coefficient continuation field 
            self.__coefficient_continuation_field = self.__get_coefficient_continuation_field(self.significand)

            tmp = ''.join([x.to01() for x in self.__coefficient_continuation_field])
            self.decimal_value = bitarray(f'{self.__sign}{self.__combination_field.to01()}{self.__exponent_continuation_field.to01()}{tmp}')
            # print(self.__combination_field)
                

    def __get_msd_representation(self, significand):
        msd = int(str(significand).zfill(34)[0])
        msd_dpd = BCD(msd)
        
        return msd_dpd
    
    def __get_exponent_representation(self, exponent):
        self.__exponent_representation = bitarray(bin(int(exponent) + self.BIAS)[2:].zfill(14))
        x = int(exponent) + self.BIAS
        print(int(exponent))
        print(x)
        print(self.__exponent_representation)
        return self.__exponent_representation

    """ TODO: Implement the __get_combination_field

    Should take in the significand and exponent (in normal base-10
    and exponent representation should be biased) and returns a bitarray
    containing the combination field
    """ 
    def __get_combination_field(self, significand: str, exponent: int) -> bitarray:
        if exponent >= 6612:
            return bitarray('11110')

        msd = self.__get_msd_representation(significand).decimal_value
        exp_representation = self.__get_exponent_representation(exponent)
        print(msd)
        
        if msd[0] == 0:
            combination_field = bitarray(
                f'{exp_representation[0]}{exp_representation[1]}{msd[1]}{msd[2]}{msd[3]}')
        elif msd[0] == 1 and msd[1] == 0 and msd[2] == 0:
            combination_field = bitarray(f'11{exp_representation[0]}{exp_representation[1]}{msd[3]}')
        
        return combination_field

    """ TODO: Implement the __get_exponent_combination_field

    Should take in the exponent (biased and in base-10) and return 
    a bitarray representing the exponent continuation field
    """
    def __get_exponent_continuation_field(self, exponent) -> bitarray:
        if exponent >= 6112:
            return bitarray(12)

        exp_representation = self.__get_exponent_representation(exponent)
        last_12_bits = exp_representation[-12:]     # Get last 12 bits
        return bitarray(last_12_bits)
    
    
    """ TODO: Implement the __get_coefficient_continuation_field

    """
    def __get_coefficient_continuation_field(self, significand) -> list[bitarray]:
        significand_str = str(significand[1:]).zfill(33)  # Pad zeroes to the left until 33 digits
        # Store significand by 3 digits in an array
        coefficient_continuation_field = [int(significand_str[i:i+3]) for i in range(0, len(significand_str), 3)]
        dpd_representation = []

        for val in coefficient_continuation_field:
            dpd_obj = DPD(str(val))
            dpd_representation.append(dpd_obj.densely_packed)

        return dpd_representation

    
    """ TODO: Override the equality function

    Should equal if all the object variables (sign, combination field, exponent 
    continuation, coefficient continuation and decimal value)
    """
    def __eq__(self, __value: "DecimalFloatingPoint") -> bool:
        return self.decimal_value ==__value.decimal_value \
            and self.exponent == __value.exponent \
            and self.significand == __value.significand \
            and self.__coefficient_continuation_field == __value.__coefficient_continuation_field\
            and self.__exponent_continuation_field == __value.__exponent_continuation_field\
            and self.__combination_field == __value.__combination_field\
            and self.__exponent_representation == __value.__exponent_representation\
            and self.__sign == __value.__sign


    """ TODO: Override the string function

    Should return the human-readable string version of the decimal value (put 
    spaces between components, i.e. sign field, combination field, exponent 
    continuation,...)
    """
    def __str__(self) -> str:
        formatted = ' '.join([x.to01() for x in self.__coefficient_continuation_field])
        return f'0b{self.decimal_value[0]} {self.decimal_value[1:6].to01()} {self.decimal_value[6:18].to01()} { formatted }'


    """ TODO: 
    """
    def to_hex(self) -> str:
        hex_string = [ch + ' ' if i % 4 == 3 else ch for i, ch in enumerate(self.decimal_value.tobytes().hex())]
        return f'0x{"".join(hex_string)}'

    
class NaNDecimalFloatingPoint(DecimalFloatingPoint):
    def __init__(self):
        self.__sign = 0  # dont care
        self.__combination_field = '11111'
        self.__exponent_continuation_field = '0000_0100_0000_0101' # dont care

        bit_array = bitarray('0010000000')
        coefficient_continuation_field = [bit_array.copy() for _ in range(10)]
        coefficient_continuation_field = tuple(coefficient_continuation_field)
        self.__coefficient_continuation_field = coefficient_continuation_field