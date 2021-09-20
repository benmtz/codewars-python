# 520446778469526ec0000001

# Complete the function/method (depending on the language) to return true/True
# when its argument is an array that has the same nesting structures
# and same corresponding length of nested arrays as the first array.
# For example:
# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

from unittest import TestCase


def are_both_sequences(x, y): return (is_sequence(x) and is_sequence(y))


def are_not_sequences(x, y): return not is_sequence(x) and not is_sequence(y)


def are_alike(x, y): return are_not_sequences(x, y) or are_both_sequences(x, y)


def is_sequence(s): return type(s) is list


def same_structure_as(original, other):
    if not are_alike(original, other):
        return False
    for idx, val in enumerate(original):
        if other[idx] is None:  # Out of bound protection
            return False
        other_val = other[idx]
        if not are_alike(val, other_val):
            return False
        if is_sequence(val) and (len(other_val) != len(val) or
                                 not same_structure_as(val, other_val)):
            return False
    return True


class TestAnagrams(TestCase):

    def test_1(self):
        self.assertEqual(same_structure_as([1, 1, 1], [2, 2, 2]), True)
        self.assertEqual(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)

        self.assertEqual(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)
        self.assertEqual(same_structure_as([1, [1, 1]], [[2], 2]), False)

        self.assertEqual(same_structure_as([[[], []]], [[[], []]]), True)

        self.assertEqual(same_structure_as([[[], []]], [[1, 1]]), False)

        self.assertEqual(same_structure_as([], 1), False)
        self.assertEqual(same_structure_as([], {}), False)

        self.assertEqual(same_structure_as([1, '[', ']'], ['[', ']', 1]), True)
