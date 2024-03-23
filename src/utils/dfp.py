from bitarray import bitarray
from enum import Enum

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
        # Setting the sign
        if significand < 0:
            self.__sign = '-'
        else:
            self.__sign = '+'
        # Setting the combination field
        __self.combination_field = self.__get_combination_field(significand, exponent)
        # Setting the exponent continuation field
        __self.exponent_continuation_field = self.__get_exponent_continuation_field(exponent)
        # Setting the coefficient continuation field 
        __self.__coefficient_continuation_field = self.__get_coefficient_continuation_field(significand)

    """ TODO: Implement the __get_combination_field

    Should take in the significand and exponent (in normal base-10
    and exponent representation should be biased) and returns a bitarray
    containing the combination field
    """ 
    def __get_combination_field(self, significand: float, exponent: int) -> bitarray:

        pass


    """ TODO: Implement the __get_exponent_combination_field

    Should take in the exponent (biased and in base-10) and return 
    a bitarray representing the exponent continuation field
    """
    def __get_exponent_continuation_field(self, exponent) -> bitarray:
        pass
    
    
    """ TODO: Implement the __get_coefficient_continuation_field

s    """
    def __get_coefficient_continuation_field(self, significand) -> list[bitarray]:
        pass

    """ TODO: Override the equality function

    Should equal if all the object variables (sign, combination field, exponent 
    continuation, coefficient continuation and decimal value)
    """
    def __eq__(self, __value: object) -> bool:
        __value: DecimalFloatingPoint


    """ TODO: Override the string function

    Should return the human-readable string version of the decimal value (put 
    spaces between components, i.e. sign field, combination field, exponent 
    continuation,...)
    """
    def __str__(self) -> str:
        pass

    """ TODO: 
    """
    def to_hex(self) -> str:
        pass
