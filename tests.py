import unittest

from number_to_words import NumbersToWords


class MyTestCase(unittest.TestCase):
    def test_compare_conversions_good_english(self):
        """
        These are tests cases in which the resulting words do have the conjunction "and"
        :return:
        """
        self.assertEqual(NumbersToWords("0", add_and=True).words, "zero")
        self.assertEqual(NumbersToWords("7", add_and=True).words, "seven")
        self.assertEqual(NumbersToWords("13", add_and=True).words, "thirteen")
        self.assertEqual(NumbersToWords("013", add_and=True).words, "thirteen")
        self.assertEqual(NumbersToWords("23", add_and=True).words, "twenty three")
        self.assertEqual(NumbersToWords("101", add_and=True).words, "one hundred and one")
        self.assertEqual(NumbersToWords("110", add_and=True).words, "one hundred and ten")
        self.assertEqual(NumbersToWords("199", add_and=True).words, "one hundred and ninety nine")
        self.assertEqual(NumbersToWords("100", add_and=True).words, "one hundred")
        self.assertEqual(NumbersToWords("1000", add_and=True).words, "one thousand")
        self.assertEqual(NumbersToWords("01000", add_and=True).words, "one thousand")
        self.assertEqual(NumbersToWords("1001", add_and=True).words, "one thousand and one")
        self.assertEqual(NumbersToWords("01001", add_and=True).words, "one thousand and one")
        self.assertEqual(NumbersToWords("10000000001", add_and=True).words, "ten billion and one")
        self.assertEqual(NumbersToWords("This is a number", add_and=True).words, "NAN")
        self.assertEqual(NumbersToWords("423", add_and=True).words, "four hundred and twenty three")
        self.assertEqual(NumbersToWords("5672", add_and=True).words, "five thousand six hundred and seventy two")
        self.assertEqual(NumbersToWords("45781", add_and=True).words,
                         "fourty five thousand seven hundred and eighty one")
        self.assertEqual(NumbersToWords("", add_and=True).words, "NAN")

    def test_compare_conversions_bad_english(self):
        """
        These are tests cases in which the resulting words do not have the conjunction "and"
        :return:
        """
        self.assertEqual(NumbersToWords("0").words, "zero")
        self.assertEqual(NumbersToWords("7").words, "seven")
        self.assertEqual(NumbersToWords("13").words, "thirteen")
        self.assertEqual(NumbersToWords("013").words, "thirteen")
        self.assertEqual(NumbersToWords("23").words, "twenty three")
        self.assertEqual(NumbersToWords("101").words, "one hundred one")
        self.assertEqual(NumbersToWords("110").words, "one hundred ten")
        self.assertEqual(NumbersToWords("199").words, "one hundred ninety nine")
        self.assertEqual(NumbersToWords("100").words, "one hundred")
        self.assertEqual(NumbersToWords("1000").words, "one thousand")
        self.assertEqual(NumbersToWords("01000").words, "one thousand")
        self.assertEqual(NumbersToWords("1001").words, "one thousand one")
        self.assertEqual(NumbersToWords("01001").words, "one thousand one")
        self.assertEqual(NumbersToWords("10000000001").words, "ten billion one")
        self.assertEqual(NumbersToWords("This is a number").words, "NAN")
        self.assertEqual(NumbersToWords("423").words, "four hundred twenty three")
        self.assertEqual(NumbersToWords("5672").words, "five thousand six hundred seventy two")
        self.assertEqual(NumbersToWords("45781").words, "fourty five thousand seven hundred eighty one")
        self.assertEqual(NumbersToWords("").words, "NAN")


if __name__ == '__main__':
    unittest.main()
