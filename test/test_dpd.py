import unittest

from bitarray import bitarray

from utils.dpd import DPD


class TestDPD(unittest.TestCase):

    bitarray_input = bitarray('1100_0101_0011', endian='big')

    def test_extract_bit__extract_start_triplet(self):
        expected = 1
        actual = DPD.extract_bit(self.bitarray_input, 'a')

        print(self.bitarray_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
        

    def test_extract_bit__extract_mid_triplet(self):
        expected = 0
        actual = DPD.extract_bit(self.bitarray_input, 'g')

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_extract_bit__extract_end_triplet(self):
        expected = 1
        actual = DPD.extract_bit(self.bitarray_input, 'l')

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
