import unittest

from bitarray import bitarray

from src.utils.dpd import *

class TestDPD(unittest.TestCase):

    bitarray_input = bitarray('1100_0101_0011', endian='big')

    def test_extract_bit__extract_start_triplet(self):
        expected = 1
        actual = DPD.extract_bit(self.bitarray_input, 'a')

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
        
    def test_987(self):
        expected = bitarray('1110001111')
        testdpd = DPD(987)
        actual = testdpd.densely_packed

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
        
    def test_007(self):
        expected = bitarray('000 0000 111')
        testdpd = DPD(7)
        actual = testdpd.densely_packed

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
        
    def test_256(self):
        expected = bitarray('010 101 0 110')
        testdpd = DPD(256)
        actual = testdpd.densely_packed

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
        
    def test_0(self):
        expected = bitarray('000 000 0 000')
        testdpd = DPD(0)
        actual = testdpd.densely_packed

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
        
    def test_52(self):
        expected = bitarray('000 101 0 010')
        testdpd = DPD(52)
        actual = testdpd.densely_packed

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
