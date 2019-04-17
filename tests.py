import unittest

from solution import NumbersToWords


class MyTestCase(unittest.TestCase):
    def test_compare_conversions(self):
        self.assertEqual(NumbersToWords("0").words, "zero")
        self.assertEqual(NumbersToWords("7").words , "seven")
        self.assertEqual(NumbersToWords("13").words , "thirteen")
        self.assertEqual(NumbersToWords("013").words , "thirteen")
        self.assertEqual(NumbersToWords("23").words , "twenty three")
        self.assertEqual(NumbersToWords("101").words , "one hundred and one")
        self.assertEqual(NumbersToWords("110").words , "one hundred and ten")
        self.assertEqual(NumbersToWords("199").words , "one hundred and ninety nine")
        self.assertEqual(NumbersToWords("100").words , "one hundred")
        self.assertEqual(NumbersToWords("1000").words , "one thousand")
        self.assertEqual(NumbersToWords("01000").words , "one thousand")
        self.assertEqual(NumbersToWords("1001").words , "one thousand and one")
        self.assertEqual(NumbersToWords("01001").words , "one thousand and one")
        self.assertEqual(NumbersToWords("10000000001").words , "ten billion and one")
        self.assertEqual(NumbersToWords("This is a number").words , "NAN")
        self.assertEqual(NumbersToWords("").words , "NAN")
        self.assertEqual(NumbersToWords("423").words , "four hundred and twenty three")
        self.assertEqual(NumbersToWords("5672").words , "five thousand six hundred and seventy two")
        self.assertEqual(NumbersToWords("45781").words , "fourty five thousand seven hundred and eighty one")


if __name__ == '__main__':
    unittest.main()
