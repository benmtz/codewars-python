# 5270d0d18625160ada0000e4
# Greed is a dice game played with five six-sided dice.
# Your mission, should you choose to accept it,
# is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.
#
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
#
# A single die can only be counted once in each roll.
# For example, a given "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points,
# but not both in the same roll.
#
# Example scoring
#
# Throw       Score
# ---------   ------------------
# 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
# 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
# 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function.
# This is something that you should never do. If you mutate the input,
# you will not be able to pass all the tests.

from unittest import TestCase


def extract_score(counts, dice_value, dice_count, value):
    result = 0
    while counts[dice_value] and (counts[dice_value] // dice_count > 0):
        counts[dice_value] = counts[dice_value] - dice_count
        result += value
    return result


def score(dice):
    result = 0
    counts = {x: len([d for d in dice if d == x]) for x in range(1, 7)}
    result += extract_score(counts, dice_value=1, dice_count=3, value=1000)
    result += extract_score(counts, dice_value=2, dice_count=3, value=200)
    result += extract_score(counts, dice_value=3, dice_count=3, value=300)
    result += extract_score(counts, dice_value=4, dice_count=3, value=400)
    result += extract_score(counts, dice_value=5, dice_count=3, value=500)
    result += extract_score(counts, dice_value=6, dice_count=3, value=600)
    result += extract_score(counts, dice_value=1, dice_count=1, value=100)
    result += extract_score(counts, dice_value=5, dice_count=1, value=50)
    return result


class Test5GreedIsGood(TestCase):

    def test_1(self):
        self.assertEqual(score([2, 3, 4, 6, 2]), 0)
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)
