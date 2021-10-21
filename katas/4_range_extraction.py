# 51ba717bb08c1cd60f00002f
#
# A format for expressing an ordered list of integers is to use a comma
# separated list of either
#
# * individual integers
# * or a range of integers denoted by the starting integer separated from
#   the end integer in the range by a dash, '-'. The range includes all
#   integers in the interval including both endpoints. It is not considered
#   a range unless it spans at least 3 numbers. For example "12,13,15-17"
#   Complete the solution so that it takes a list of integers in
#   increasing order and returns a correctly formatted string in the range
#   format.
#
# Example:
#
# solution(
#  [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
# )
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"
from itertools import groupby
import unittest
from unittest import TestCase


def stringify_pair(r):
    if r[0] == r[1]:
        return str(r[0])
    elif r[1] - r[0] >= 2:
        return f"{r[0]}-{r[1]}"
    else:
        return ",".join([str(u) for u in range(r[0], r[1] + 1)])


def stringify_ranges(ranges):
    return ",".join([stringify_pair(x) for x in ranges])


def ranges(integers):
    def group_by_function(pair):
        return pair[1] - pair[0]

    # It's brilliant, but sadly not mine, found it here :
    # https://stackoverflow.com/questions/4628333/converting-a-list-of-integers-into-range-in-python
    # However it may be error prone in real world code
    for a, b in groupby(enumerate(integers), group_by_function):
        # This makes a subgroup calling the grouper once again
        b = list(b)
        yield b[0][1], b[-1][1]


def solution(args):
    return stringify_ranges(ranges(args))


class SolutionTest(TestCase):

    def test_basic_cases(self):
        self.assertEqual(solution(
            [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18,
             19, 20]
        ), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]),
                         '-3--1,2,10,15,16,18-20')


if __name__ == "__main__":
    unittest.main()
