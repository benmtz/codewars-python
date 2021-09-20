import unittest


def make_readable(seconds):
    return "{hours:02d}:{minutes:02d}:{seconds:02d}".format(
        hours=int(seconds / 3600),
        minutes=int(seconds / 60) % 60,
        seconds=seconds % 60
    )


class TestMakeReadable(unittest.TestCase):
    def test_1(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")
