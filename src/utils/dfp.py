from bitarray import bitarray
from src.utils.RoundingMethod import RoundingMethod
from src.utils.bcd import BCD
from src.utils.dpd import DPD
import src.utils.utils as dfp_utils
from decimal import Decimal


class DecimalFloatingPoint:
    
    BIAS: int = 6176
    E_MAX: int = 6111
    E_MIN: int = -6176

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
        sign, significand, exponent = dfp_utils.normalize_significand(
            significand, exponent, rounding_method)
        
        self.__sign = sign
        self.significand = significand
        self.exponent = Decimal(exponent)
        self.rounding_method = rounding_method
    
        self.__combination_field = self.__get_combination_field(self.significand, self.exponent)

        self.__exponent_continuation_field = self.__get_exponent_continuation_field(self.exponent, self.significand)

        self.__coefficient_continuation_field = self.__get_coefficient_continuation_field(self.significand, self.exponent)

        tmp = ''.join([x.to01() for x in self.__coefficient_continuation_field])
        self.decimal_value = bitarray(f'{self.__sign}{self.__combination_field.to01()}{self.__exponent_continuation_field.to01()}{tmp}')
                

    def __get_msd_representation(self, significand):
        msd = int(str(significand).zfill(34)[0])
        msd_dpd = BCD(msd)
        
        return msd_dpd
    
    def __get_exponent_representation(self, exponent):
        self.__exponent_representation = bitarray(bin(int(exponent) + self.BIAS)
                                                  .lstrip('+')
                                                  .lstrip('-')
                                                  .lstrip('0b')
                                                  .zfill(14))
        print(exponent + self.BIAS)
        print(exponent + self.BIAS)
        print(bin(int(exponent) + self.BIAS).lstrip('+')
                                                  .lstrip('-')
                                                  .zfill(14))
        return self.__exponent_representation

    """ TODO: Implement the __get_combination_field

    Should take in the significand and exponent (in normal base-10
    and exponent representation should be biased) and returns a bitarray
    containing the combination field
    """ 
    def __get_combination_field(self, significand: str, exponent: int) -> bitarray:

        if Decimal(significand) != 0 and self.is_infinity(exponent):
            return bitarray('11110')

        msd = self.__get_msd_representation(significand).decimal_value

        if Decimal(significand) == 0:
            exp_representation = self.__get_exponent_representation(0)
            print("exp: " + str(exp_representation))
        else: 
            exp_representation = self.__get_exponent_representation(exponent)
        
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
    def __get_exponent_continuation_field(self, exponent, significand=None) -> bitarray:

        if significand is not None and Decimal(significand) != 0 and self.is_infinity(exponent):
            return bitarray(12)
        
        if significand is not None and Decimal(significand) == 0:
            exponent = 0

        exp_representation = self.__get_exponent_representation(exponent)
        last_12_bits = exp_representation[-12:]     # Get last 12 bits
        return bitarray(last_12_bits)
    
    
    """ TODO: Implement the __get_coefficient_continuation_field

    """
    def __get_coefficient_continuation_field(self, significand, exponent=None) -> list[bitarray]:

        if self.is_infinity(exponent) or Decimal(self.significand) == 0:
            return [ bitarray(10) for _ in range(11) ]

        significand_str = str(significand[1:]).zfill(33)  # Pad zeroes to the left until 33 digits
        # Store significand by 3 digits in an array
        coefficient_continuation_field = [int(significand_str[i:i+3]) for i in range(0, len(significand_str), 3)]
        dpd_representation = []

        for val in coefficient_continuation_field:
            dpd_obj = DPD(str(val))
            dpd_representation.append(dpd_obj.densely_packed)

        return dpd_representation

    def is_infinity(self, exponent):
        return exponent > self.E_MAX or exponent < self.E_MIN

    
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
        self.__combination_field = bitarray('11111')
        self.__exponent_continuation_field = bitarray('0000_0100_0000_0101') # dont care

        bit_array = bitarray('0010000000')
        coefficient_continuation_field = [bit_array.copy() for _ in range(10)]
        coefficient_continuation_field = tuple(coefficient_continuation_field)
        self.__coefficient_continuation_field = coefficient_continuation_field

        tmp = ''.join([x.to01() for x in self.__coefficient_continuation_field])
        self.decimal_value = bitarray(f'{self.__sign}{self.__combination_field.to01()}{self.__exponent_continuation_field.to01()}{tmp}')

    def __str__(self) -> str:
        formatted = ' '.join([x.to01() for x in self.__coefficient_continuation_field])
        return f'0b{self.decimal_value[0]} {self.decimal_value[1:6].to01()} {self.decimal_value[6:18].to01()} { formatted }'

    def to_hex(self) -> str:
        hex_string = [ch + ' ' if i % 4 == 3 else ch for i, ch in enumerate(self.decimal_value.tobytes().hex())]
        return f'0x{"".join(hex_string)}'
    