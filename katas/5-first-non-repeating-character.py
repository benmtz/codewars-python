import unittest

# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the
# string. As an added challenge, upper- and lowercase letters are considered
# the same character, but the function should return the correct case for the
# initial letter. For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty
# string ("") or None -- see sample tests.


def first_non_repeating_letter(word):
    def is_repeating_in_word(letter):
        return word.upper().count(letter.upper()) == 1
    return next(filter(is_repeating_in_word, word), '')


class TestFirstNonRepeatingLetter(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(first_non_repeating_letter('a'), 'a')
        self.assertEquals(first_non_repeating_letter('stress'), 't')
        self.assertEquals(first_non_repeating_letter('moonmen'), 'e')

    def test_should_handle_empty_strings(self):
        self.assertEquals(first_non_repeating_letter(''), '')

    def test_should_handle_all_repeating_strings(self):
        self.assertEquals(first_non_repeating_letter('abba'), '')
        self.assertEquals(first_non_repeating_letter('aa'), '')

    def test_should_handle_odd_characters(self):
        self.assertEquals(first_non_repeating_letter('~><#~><'), '#')
        self.assertEquals(first_non_repeating_letter('hello world, eh?'), 'w')

    def test_should_handle_letter_cases(self):
        self.assertEquals(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEquals(
            first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!"),
            ','
        )
