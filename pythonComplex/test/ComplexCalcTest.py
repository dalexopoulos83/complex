import unittest
from pythonComplex.app.ComplexNum import ComplexNum


class ComplexCalcTest(unittest.TestCase):

    def setUp(self):
        self.cn1 = ComplexNum(3, 7)
        self.cn2 = ComplexNum(3, 7)
        self.cn3 = ComplexNum(1, 1)

    def test_calculator_add_method_returns_correct_result(self):
        result = self.cn1 + self.cn2
        self.assertEqual("6+14j", str(result))

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.cn1 - self.cn2
        self.assertEqual("0+0j", str(result))

    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.cn1 * self.cn2
        self.assertEqual("-40+42j", str(result))

    def test_calculator_multiply_with_real_method_returns_correct_result(self):
        result = self.cn1 * 4
        self.assertEqual("12+28j", str(result))

    def test_calculator_multiply_with_3_comple_method_returns_correct_result(self):
        result = self.cn1 * self.cn2 * self.cn3
        self.assertEqual("-82+2j", str(result))

    def test_calculator_divide_method_returns_correct_result(self):
        result = self.cn1 / self.cn2
        self.assertEqual("1.000000+0.000000j", str(result))

    def test_calculator_divide_complex_with_real_method_returns_correct_result(self):
        result = self.cn1 / 4
        self.assertEqual("0.750000+1.750000j", str(result))

    def test_calculator_exp_method_returns_correct_result(self):
        result = self.cn1 ** 3
        self.assertEqual("-414-154j", str(result))

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.failUnlessRaises(ValueError, ComplexNum, "one", "two")


if __name__ == '__main__':
    unittest.main()
