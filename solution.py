import re


class NumbersToWords(object):

    def __init__(self, number: str, add_and=False):
        """
        Given any number up to a vigintillion, this class will return the same number in words
        :param number: The interger number to convert to words
        :param add_and: if you want good English, change add_and to True
        :type number: str
        """
        self.add_and = add_and

        if re.match(r"^\d+$", number):

            thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
                         'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion',
                         'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'sexdecillion',
                         'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']

            self.words = []

            # split the number into groups of thousandths
            groups = "{:,}".format(int(number)).split(",")

            # print(groups)
            group_count = len(groups)
            if group_count > 1:

                # convert the matched group  to words
                for index, group in enumerate(groups):
                    words = self.convert(group)
                    if words != "zero":

                        # only for the last group, add an and if necessary
                        if index == group_count - 1 and group[0] == "0" and add_and:
                            self.words.append("and")

                        self.words.append(words)
                        self.words.append(thousands[group_count - index - 1])
            else:
                # we only have one group
                self.words.append(self.convert(number))

            self.words = (' '.join(self.words)).strip()
        else:
            self.words = "NAN"

    def convert(self, number: str):
        """
        This is the entry point for converting 3 digit numbers (max) to words
        :param number:
        :return:
        """
        words = ""
        number = re.sub(r"^(0*)", "", number)

        if number == "":
            words = "zero"
        elif re.match(r'[1-9]\d*', number):
            if len(number) == 1:
                words = self.single_digits(number)
            elif len(number) == 2:
                words = self.two_digits(number)
            elif len(number) == 3:
                words = self.three_digits(number)

            words = ' '.join(words.split())
        return words

    def single_digits(self, digit: str):
        """
        Given a single digit, return the digit equivalent in words
        :param digit:
        :return:
        """
        if digit == "0":
            return ''
        ones = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
        }
        return ones[digit]

    def two_digits(self, digits: str):
        """
        Given two digits, return the tenths equivalent in words
        :param digits:
        :return:
        """
        words = []
        tens = {
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
            "20": "twenty",
            "30": "thirty",
            "40": "fourty",
            "50": "fifty",
            "60": "sixty",
            "70": "seventy",
            "80": "eighty",
            "90": "ninety"
        }

        if digits in tens:
            return tens[digits]
        elif digits[0] == "0":
            return self.single_digits(digits[1:])
        else:
            words.append(tens[f"{digits[0]}0"])
            words.append(self.single_digits(digits[1]))
            return ' '.join(words)

    def three_digits(self, digits: str):
        """
        Given three digits, return the hundredths equivalent in words
        :param digits:
        :return:
        """
        words = []
        first_digit = digits[0]

        if first_digit == "0":
            return self.two_digits(digits[1:])
        else:
            start = self.single_digits(first_digit)
            words.append(f"{start} hundred ")
            others = self.two_digits(digits[1:])
            if others and self.add_and:
                words.append(f"and {others}")
            else:
                words.append(f"{others}")
        return ' '.join(words)
