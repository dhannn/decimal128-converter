from bitarray import bitarray

from src.utils.bcd import BCD

class DPD:
    
    original_value: int
    sign: str
    densely_packed: bitarray
    input_char_to_index = { chr(i + ord('a')): i for i in range(12) }
    output_char_to_index = { chr(i + ord('p')): i for i in range(12) }

    output_mapping = {
        '000': lambda x: bitarray([x['b'], x['c'], x['d'], x['f'], x['g'], x['h'], 0, x['j'], x['k'], x['l']]),
        '001': lambda x: bitarray([x['b'], x['c'], x['d'], x['f'], x['g'], x['h'], 1, 0, 0, x['l']]),
        '010': lambda x: bitarray([x['b'], x['c'], x['d'], x['j'], x['k'], x['h'], 1, 0, 1, x['l']]),
        '100': lambda x: bitarray([x['j'], x['k'], x['d'], x['f'], x['g'], x['h'], 1, 1, 0, x['l']]),
        '110': lambda x: bitarray([x['j'], x['k'], x['d'], 0, 0, x['h'], 1, 1, 1, x['l']]),
        '101': lambda x: bitarray([x['f'], x['g'], x['d'], 0, 1, x['h'], 1, 1, 1, x['l']]),
        '011': lambda x: bitarray([x['b'], x['c'], x['d'], 1, 0, x['h'], 1, 1, 1, x['l']]),
        '111': lambda x: bitarray([0, 0, x['d'], 1, 1, x['h'], 1, 1, 1, x['l']])
    }

    def __init__(self, val: str):
        bcd_value = BCD(val)
        self.original_value = val

        bit_components = {
            chr(component): 
            DPD.extract_bit(bcd_value.decimal_value, chr(component))
            for component in range(ord('a'), ord('l') + 1)
        }

        aei = bitarray([bit_components['a'], bit_components['e'], bit_components['i']]).to01() # extract msb of each 4 bits

        # For checking:
        # print("val", self.original_value)
        # print("aei: ", aei)
        # print("densely packed bcd: ", self.output_mapping[aei](bit_components))
        
        output_bits = self.output_mapping[aei](bit_components)
        self.densely_packed = output_bits

    @staticmethod
    def extract_bit(bits: bitarray, char_index: str):
        index = DPD.input_char_to_index[char_index]
        padded_bits = bitarray(bits.to01().zfill(12))
        return padded_bits[index]
    