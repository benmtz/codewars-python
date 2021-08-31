# 54a91a4883a7de5d7800009c
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#   foo -> foo1
#   foobar23 -> foobar24
#   foo0042 -> foo0043
#   foo9 -> foo10
#   foo099 -> foo100
# Attention: If the number has leading zeros the amount of digits should be considered.

import unittest
import re

def increment_string(strng):
    splited = re.split("(\d+)$", strng)
    ending_digits = splited[1] if len(splited) > 2 else "0"
    pad_digit_token = "0{PadTo}".format(PadTo = len(ending_digits))
    return "{0}{1}".format(splited[0], format(int(ending_digits)+1, pad_digit_token))

class TestAnagrams(unittest.TestCase):

    def test_1(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string(""), "1")

if __name__ == '__main__':
    unittest.main()
