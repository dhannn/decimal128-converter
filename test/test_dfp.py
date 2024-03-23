import unittest

from utils.dfp import *

class TestDFP(unittest.TestCase):

    """ TODO: Generate test cases for the DecimalFloatingPoint class

    Make sure to have good coverage (scenarios should span different cases
    such as different rounding methods, positive, negative, largest possible,
    smallest possible, zeroes, ...)
    """

    def test_NormalPositive(self):
        _input = 11_1234_5678_9012_3456_7890_1234_5678_9012
        expected = bitarray('0_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010') 
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_TNE)

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')

    def test_NormalNegative(self):
        _input = -11_1234_5678_9012_3456_7890_1234_5678_9012
        expected = bitarray('1_01001_0111_1101_1010_001_001_0010_011_100_0101_110_111_1000_001_000_1101_010_011_0100_101_110_0111_000_001_1110_001_010_0011_100_101_0110_111_100_1111_000_001_0010')
        actual = DecimalFloatingPoint(_input, -70, RoundingMethod.ROUND_TNE)

        self.assertEqual(expected, actual,
                    f'Expected is { expected }, returns { actual }')
