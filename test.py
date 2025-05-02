import unittest

from convert import to_arabic, to_roman

class TestConvert(unittest.TestCase):
    def test_to_arabic(self):
        # 1918, the first year of the Spanish flu pandemic
        n = "MCMXVIII"
        self.assertEqual(to_arabic(n), 1918)

    def test_to_roman(self):
        n = 1918
        self.assertEqual(to_roman(n), "MCMXVIII")