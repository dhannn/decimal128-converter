import unittest

from src.utils.RoundingMethod import RoundingMethod
from src.utils.utils import *
from src.utils.dfp import *

class TestUtils(unittest.TestCase):

    SIGFIGS = 5
    EXP = 0

    def __test(self, significand, expected_sign, expected_significand, expected_exponent):
        actual_sign, actual_significand, actual_exponent = normalize_significand(
            significand, self.EXP, RoundingMethod.ROUND_TNE, self.SIGFIGS
        )

        self.assertEqual(
            expected_sign, actual_sign
        )

        self.assertEqual(
            expected_significand, actual_significand, 
            f'Expected {expected_significand}, returns {actual_significand}')
        
        self.assertEqual(
            expected_exponent, actual_exponent
        )

    def test__zeroes(self):
        self.__test('00', 0, '00000', '0')

    def test__withinSignificantDigits_Positive_NoDecimal(self):
        significand = '12'

        expected_sign = 0
        expected_significand = '00012'
        expected_exponent = '0'

        self.__test(significand, expected_sign, expected_significand, expected_exponent)


    def test__withinSignificantDigits_Negative_NoDecimal(self):
        self.__test('-123', 1, '00123', '0')

    def test__withinSignificantDigits_Positive_WithDecimal(self):
        self.__test('+123.4', 0, '01234', '-1')

    def test__withinSignificantDigits_Negative_WithDecimal(self):
        self.__test('-1.23', 1, '00123', '-2')

    def test__exactlySignificantDigits_NoDecimal(self):
        self.__test('-12345', 1, '12345', '0')

    def test__exactlySignificantDigits_WithDecimal(self):
        self.__test('0.12345', 0, '12345', '-5')
    
    def test__beyondSignificantDigits_DecimalWithinMostSignificant(self):
        self.__test('123.4567', 0, '12346', '-2')

    def test__beyondSignificantDigits_DecimalBeyondMostSignificant(self):
        self.__test('-1234567.89', 1, '12346', '2')

    def test__beyondSignificantDigits_Positive_WithDecimal(self):
        pass

    def test__beyondSignificantDigits_Negative_WithDecimal(self):
        pass

    def test__roundOff_RoundNearest_RoundingUp(self):
        self.__test_rounding('123456', RoundingMethod.ROUND_TNE, '12346', 5)

    def test__roundOff_RoundNearest_RoundingDown(self):
        self.__test_rounding('123451234', RoundingMethod.ROUND_TNE, '12345', 5)
    
    def test__roundOff_RoundNearest_Negative(self):
        self.__test_rounding('123456', RoundingMethod.ROUND_TNE, '12346', 5, 1)
    
    def test__roundUp_Positive(self):
        self.__test_rounding('1234567', RoundingMethod.ROUND_UP, '12346', 5)
    
    def test__roundUp_Negative(self):
        self.__test_rounding('1234567', RoundingMethod.ROUND_UP, '12345', 5, 1)
    
    def test__roundDown_Positive(self):
        self.__test_rounding('1234567', RoundingMethod.ROUND_DOWN, '12345', 5, 0)
    
    def test__roundDown_Negative(self):
        self.__test_rounding('1234567', RoundingMethod.ROUND_DOWN, '12346', 5, 1)

    def __test_rounding(self, number, rounding_method: RoundingMethod, expected_significand, expected_offset, sign=0):
        actual_significand, actual_offset = round_off(number, self.SIGFIGS, rounding_method, sign=sign)

        self.assertEqual(
            expected_significand, actual_significand
        )

        self.assertEqual(
            expected_offset, actual_offset
        )
