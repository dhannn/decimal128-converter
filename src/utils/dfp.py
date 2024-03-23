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
        # Normalizing the significand to 34 digits
        # Counting significand's number of digits, excluding sign and decimal point
        total_digits = sum(1 for char in str(abs(number)) if char.isdigit())
        # If significand has more than 34 digits, move the decimal place after the 34th digit
        if total_digits > 34:
            digits_to_move = total_digits - 34          # Determine number of digits to move
            significand *= 10 ** digits_to_move         # Move decimal point
            exponent -= digits_to_move                  # Update exponent

            significand_str = str(abs(significand))
            decimal_index = significand_str.find('.')   # Find the index of the decimal point
            if decimal_index != -1:                     # If decimal point exists
                digits_after_decimal = significand_str[decimal_index + 1:]
                num_digits_after_decimal = len(significand_str) - decimal_index - 1
                # Determine rounding method
                rounding_base = 10 ** num_digits_after_decimal
                half_rounding_base = rounding_base // 2
                
                if int(digits_after_decimal) > half_rounding_base:
                    self.rounding_method = ROUND_UP
                    significand = self.__round_off(ROUND_UP, significand)
                elif int(digits_after_decimal) < half_rounding_base:
                    self.rounding_method = ROUND_DOWN
                    significand = self.__round_off(ROUND_DOWN, significand)
                else:
                    self.rounding_method = ROUND_TNE
                    significand = self.__round_off( ROUND_TNE, significand)
            
        # If number of digits is less than 34, pad zeroes to the left
        elif total_digits < 34:
            digits_to_move = 0
            while total_digits < 34:
                significand *= 10
                exponent -= 1
                total_digits += 1
                digits_to_move += 1
            significand_str = str(abs(significand))
            significand_str = significand_str.zfill(34)
            significand = int(significand_str)
            
        elif total_digits == 34:
            digits_to_move = total_digits - 34          # Determine number of digits to move
            significand *= 10 ** digits_to_move         # Move decimal point
            exponent -= digits_to_move      
        
        # Setting the sign
        self.__sign = '+' if self.original_value >= 0 else '-'

        # Setting the combination field
        self.__combination_field = self.__get_combination_field(significand, exponent)
        # Setting the exponent continuation field
        self.__exponent_continuation_field = self.__get_exponent_continuation_field(exponent)
        # Setting the coefficient continuation field 
        self.__coefficient_continuation_field = self.__get_coefficient_continuation_field(significand)

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

    """
    def __get_coefficient_continuation_field(self, significand) -> list[bitarray]:
        pass


    """ TODO: Implement __round_off

    Given a float value, perform the appropriate rounding method such that it reaches 34 values
    """
    def __round_off(self, rounding_method, val) -> float:
        final_val = 0
        val_str = str(val)
        digits_to_keep = min(len(val_str), 34)  
        last_digits = val_str[-digits_to_keep:]
        last_digits_int = int(last_digits)
        keep_digits_int = int(val)

        if rounding_method == ROUND_UP:
            return val + 1
        elif rounding_method == ROUND_DOWN:
            return val
        elif rounding_method == ROUND_TNE:
            if keep_digits_int % 2 == 1:        # if odd
                return val + 1
            else:                               # if even
                return val

    
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
