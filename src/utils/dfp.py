from bitarray import bitarray
from enum import Enum
from src.utils.bcd import BCD
from src.utils.dpd import DPD 

from src.utils.dpd import DPD

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
    def __init__(self, significand: float, exponent: int, rounding_method):

        # Normalizing the significand to 34 digits
        # Counting significand's number of digits, excluding sign and decimal point
        total_digits = sum(1 for char in significand if char.isdigit())
        # If significand has more than 34 digits, move the decimal place after the 34th digit
        significand_str = significand
        if total_digits > 34:
            digits_to_move = total_digits - 34          # Determine number of digits to move
            significand *= 10 ** digits_to_move         # Move decimal point
            exponent -= digits_to_move                  # Update exponent

            decimal_index = significand_str.find('.')   # Find the index of the decimal point
            if decimal_index != -1:                     # If decimal point exists                
                if rounding_method == RoundingMethod.ROUND_UP:
                    significand = self.__round_off(RoundingMethod.ROUND_UP, significand)
                elif rounding_method == RoundingMethod.ROUND_DOWN:
                    self.rounding_method = RoundingMethod.ROUND_DOWN
                    significand = self.__round_off(RoundingMethod.ROUND_DOWN, significand)
                elif rounding_method == RoundingMethod.ROUND_TNE:
                    significand = self.__round_off(RoundingMethod.ROUND_TNE, significand)
            
        # If number of digits is less than 34
        elif total_digits < 34:
            digits_to_move = 0
            while total_digits < 34:
                significand *= 10
                exponent -= 1
                total_digits += 1
                digits_to_move += 1
            significand = int(float(significand_str))

        # If number of digits is 34
        elif total_digits == 34:
            digits_to_move = total_digits - 34          # Determine number of digits to move
            significand *= 10 ** digits_to_move         # Move decimal point
            exponent -= digits_to_move
        
        self.significand = significand
        self.exponent = int(exponent)
        self.rounding_method = rounding_method
        
        # Setting the sign
        self.__sign = 0 if self.significand >= 0 else 1
        # Setting the combination field
        self.__combination_field = self.__get_combination_field(significand, exponent)
        # Setting the exponent continuation field
        self.__exponent_continuation_field = self.__get_exponent_continuation_field(exponent)
        # Setting the coefficient continuation field 
        self.__coefficient_continuation_field = self.__get_coefficient_continuation_field(significand)

        tmp = ''.join([x.to01() for x in self.__coefficient_continuation_field])
        self.decimal_value = bitarray(f'{self.__sign}{self.__combination_field.to01()}{self.__exponent_continuation_field.to01()}{tmp}')
        # print(self.__combination_field)

        def normalize_significand(significand: str, exponent):
            significand = '0' + significand

            for i in range(len(significand)):
                index = len(significand) - i - 1
                digit = significand[index]

                if digit != '0':
                    break

                exponent += 1
            
            parts = significand.split('.')
            exponent = exponent - len(parts[1])

            significand = parts[0].zfill(34)
            return significand, exponent
                

    def __get_msd_representation(self, significand):
        msd = int(str(significand).zfill(34)[0])
        msd_dpd = BCD(msd)
        
        return msd_dpd
    
    def __get_exponent_representation(self, exponent):
        self.__exponent_representation = bitarray(bin(int(exponent) + self.BIAS)[2:].zfill(14))
        x= int(exponent) + self.BIAS
        print(int(exponent))
        print(x)
        print(self.__exponent_representation)
        return self.__exponent_representation

    """ TODO: Implement the __get_combination_field

    Should take in the significand and exponent (in normal base-10
    and exponent representation should be biased) and returns a bitarray
    containing the combination field
    """ 
    def __get_combination_field(self, significand: float, exponent: int) -> bitarray:
        if exponent >= 6612:
            return bitarray('11110')

        msd = self.__get_msd_representation(significand).decimal_value
        exp_representation = self.__get_exponent_representation(exponent)
        
        if msd[0] == 0:
            combination_field = bitarray(
                f'{exp_representation[0]}{exp_representation[1]}0{msd[1]}{msd[2]}{msd[3]}')
        elif msd[0] == 1 and msd[1] == 1:
            combination_field = bitarray(f'11{exp_representation[0]}{exp_representation[1]}100{msd[3]}')
        
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
        significand_str = str(significand).zfill(33)  # Pad zeroes to the left until 33 digits
        # Store significand by 3 digits in an array
        coefficient_continuation_field = [int(significand_str[i:i+3]) for i in range(0, len(significand_str), 3)]
        dpd_representation = []

        for val in coefficient_continuation_field:
            dpd_obj = DPD(str(val))
            dpd_representation.append(dpd_obj.densely_packed)

        return dpd_representation


    """ TODO: Implement __round_off

    Given a float value, perform the appropriate rounding method such that it reaches 34 values
    """
    def __round_off(self, rounding_method, val) -> float:
        val_str = str(val)
        digits_to_keep = min(len(val_str), 34)  
        # last_digits = val_str[-digits_to_keep:]
        # last_digits_int = int(last_digits)
        keep_digits_int = int(val)

        if rounding_method == RoundingMethod.ROUND_UP:
            return val + 1
        elif rounding_method == RoundingMethod.ROUND_DOWN:
            return val
        elif rounding_method == RoundingMethod.ROUND_TNE:
            if keep_digits_int % 2 == 1:        # if odd
                return val + 1
            else:                               # if even
                return val

    
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
        return f'0b{self.decimal_value[0]} {self.decimal_value[1:6].to01()} {self.decimal_value[6:17].to01()} { formatted }'


    """ TODO: 
    """
    def to_hex(self) -> str:
        hex_string = self.decimal_value.tobytes().hex()
        return f'0x{hex_string}'

    
class NaNDecimalFloatingPoint(DecimalFloatingPoint):
    def __init__(self):
        self.__sign = 0  # dont care
        self.__combination_field = '11111'
        self.__exponent_continuation_field = '0000_0100_0000_0101' # dont care

        bit_array = bitarray('0010000000')
        coefficient_continuation_field = [bit_array.copy() for _ in range(10)]
        coefficient_continuation_field = tuple(coefficient_continuation_field)
        self.__coefficient_continuation_field = coefficient_continuation_field