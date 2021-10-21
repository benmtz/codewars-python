from collections.abc import Sequence
from unittest import TestCase


def anagram_matcher_factory(w1: str):
    _w1 = list(w1)
    _w1.sort()

    def is_anagram(w2: str):
        _w2 = list(w2)
        _w2.sort()
        return _w1 == _w2

    return is_anagram


def anagrams(word: str, words: Sequence[str]):
    return list(filter(anagram_matcher_factory(word), words))


class TestAnagrams(TestCase):

    def test_1(self):
        self.assertEqual(
            anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']),
            ['aabb', 'bbaa'],
            "Array differ"
        )

    def test_2(self):
        self.assertEqual(
            anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']),
            ['carer', 'racer'],
            "Array differ"
        )
