import unittest

from src.utils.bcd import *

class TestBCD(unittest.TestCase):

    def test_IntPositive(self):
        _input = 8
        expected = MockBCD(_input, '+', bitarray('1000'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_IntNegative(self):
        _input = -2
        expected = MockBCD(_input, '-', bitarray('0010'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_IntZero(self):
        _input = 0
        expected = MockBCD(_input, '+', bitarray('0000'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_IntMoreThanThreeDigits(self):
        _input = 12089
        expected = MockBCD(_input, '+', bitarray('0001 0010 0000 1000 1001'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_StrPositive(self):
        _input = '468'
        expected = MockBCD(int(_input), '+', bitarray('0100 0110 1000'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_StrNegative(self):
        _input = '-102'
        expected = MockBCD(int(_input), '-', bitarray('0001 0000 0010'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')

    def test_StrMoreThanThreeDigits(self):
        _input = '-999888777'
        expected = MockBCD(int(_input), '-', bitarray('1001 1001 1001 1000 1000 1000 0111 0111 0111'))
        actual = BCD(_input)

        self.assertEqual(expected, actual,
                         f'Expected is { expected }, returns { actual }')
