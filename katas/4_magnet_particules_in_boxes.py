from unittest import TestCase
from functools import lru_cache


@lru_cache(maxsize=None)
def cached_pow(nb, pow):
    return nb ** pow

@lru_cache(maxsize=None)
def box_force(k, n):
    return 1 / (k * cached_pow(n + 1, 2 * k))


def doubles(maxk, maxn):
    return sum([box_force(k, n) for k in range(1, maxk + 1) for n in range(1, maxn + 1)])


class TestDoubles(TestCase):

    def assertFuzzyEquals(self, actual, expected, msg=""):
        merr = 1e-9
        msg = "Tested at 1e-9; Expected value must be {:0.16f} but got {:0.16f}".format(expected, actual)
        return self.assertAlmostEqual(actual, expected, delta=merr, msg=msg)

    def test_box_force(self):
        self.assertEqual(box_force(1, 1), 0.25)

    def test_basic(self):
        self.assertFuzzyEquals(doubles(20, 10000), 0.6930471955575918)

    def test_basic_2(self):
        self.assertFuzzyEquals(doubles(1, 10), 0.5580321939764581)
        self.assertFuzzyEquals(doubles(10, 1000), 0.6921486500921933)
        self.assertFuzzyEquals(doubles(10, 10000), 0.6930471674194457)


    def test_long(self):
        doubles(40, 150000)
