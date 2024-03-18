from bitarray import bitarray


class DecimalFloatingPoint:

    BIAS: int = 6176

    original_value: float
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
    def __init__(self, value: str | float | int):
        pass


    """ TODO: Implement the __get_combination_field

    Should take in the significand and exponent (in normal base-10
    and exponent representation should be biased) and returns a bitarray
    containing the combination field
    """
    def __get_combination_field(self, significand, exponent) -> bitarray:
        pass


    """ TODO: Implement the __get_exponent_combination_field

    Should take in the exponent (biased and in base-10) and return 
    a bitarray representing the exponent continuation field
    """
    def __get_exponent_continuation_field(self, exponent) -> bitarray:
        pass
    
    
    """ TODO: Implement the __get_coefficient_continuation_field

    Same as the exponent continuation but returns a list of bitarrays
    representing each triplet of the few least significant digits of 
    the mantissa/significand (in densely-packed)
    """
    def __get_coefficient_continuation_field(self, significand) -> list[bitarray]:
        pass

    """ TODO: Override the equality function

    Should equal if all the object variables (sign, combination field, exponent 
    continuation, coefficient continuation and decimal value)
    """
    def __eq__(self, __value: object) -> bool:
        __value: DecimalFloatingPoint


    """ TODO: Override the string function

    Should return the human-readable string version of the  decimal value.
    """
    def __str__(self) -> str:
        pass
