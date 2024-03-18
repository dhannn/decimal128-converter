from bitarray import bitarray 


class BCD:

    original_value: int
    sign: str
    nibbles: list[bitarray]
    decimal_value: bitarray

    def __init__(self, val: int | str) -> None:
        pass
        if type(val) == str:
            val = int(val)
        
        self.original_value = int(val)
        self.sign = '+' if val >= 0 else '-'

        nibbles = []

        val = abs(val)
        if val == 0:
            nibbles.append(bitarray(''.zfill(4)))

        while val > 0:
            digit = val % 10
            nibbles.insert(0, bitarray(bin(digit)[2:].zfill(4)))
            val //= 10
        
        self.nibbles = nibbles
        self.decimal_value = bitarray(
            ''.join([nibble.to01() for nibble in nibbles]))

    def __eq__(self, __value: object) -> bool:
        __value: BCD
        return self.sign == __value.sign and\
            self.decimal_value == __value.decimal_value and\
            self.original_value == __value.original_value

    def __str__(self) -> str:
        return f'{ self.sign }{ self.decimal_value.to01() }'

    
class MockBCD(BCD):

    def __init__(self, val, sign, dec) -> None:
        self.original_value = val
        self.sign = sign
        self.decimal_value = dec
