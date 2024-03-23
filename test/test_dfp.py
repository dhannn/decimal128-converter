import unittest

from bitarray import bitarray
from src.utils.dfp import *

class TestDFP(unittest.TestCase):

    """ TODO: Generate test cases for the DecimalFloatingPoint class

    Make sure to have good coverage (scenarios should span different cases
    such as different rounding methods, positive, negative, largest possible,
    smallest possible, zeroes, ...)
    """

    def test_NormalPositive(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678_9012
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010') 
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')

    def test_NormalNegative(self):
        _input = -11_1234_5678_9012_3456_7890_1234_5678_9012
        expected = bitarray('1_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010')
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_InfinityPositive(self):
        _input = 1
        expected = bitarray('0111 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000')
        actual = DecimalFloatingPoint(_input, 6112, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_InfinityNegative(self):
        _input = -1
        expected = bitarray('1111 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000')
        actual = DecimalFloatingPoint(_input, 6112, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_ZeroPositive(self):
        _input = 0
        expected = bitarray('0010 0010 0000 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000')
        actual = DecimalFloatingPoint(_input, 6112, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_ZeroNegative(self):
        _input = -0
        expected = bitarray('1010 0010 0000 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000')
        actual = DecimalFloatingPoint(_input, 6112, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_NormalPositiveWithDecimal(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678_9012.5
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010')
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_NormalPositiveWithDecimal(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678_9012.5
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0011')
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_UP).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_NormalPositiveWithDecimal(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678_9012.5
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010')
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_DOWN).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
        
    def test_DenormalizedNormalPositiveWithDecimal(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678.901251
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0011')
        actual = DecimalFloatingPoint(_input, -66, RoundingMethod.ROUND_TNE).decimal_value

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
