import unittest

from Concept_Question1 import is_isogram, OverOneWord


class TestIsIsogram(unittest.TestCase):
# situations to be True
    def test_isogram_word(self):
        # A word with no repeated letters should be considered an isogram
        self.assertTrue(is_isogram("tear"))

    def test_mixed_case_word(self):
        # A word with no repeated letters with mixed case should be considered as an isogram
        self.assertTrue(is_isogram("Pycharm"))

    def test_single_letter(self):
        # A single letter should be considered an isogram
        self.assertTrue(is_isogram("a"))

# Siuations to be False
    def test_non_isogram_word(self):
        # A word with repeated letters should not be considered an isogram
        self.assertFalse(is_isogram("hello"))

    def test_whitespace(self):
        # Input containing more than one word should raise OverOneWord exception
        self.assertRaises(OverOneWord, is_isogram, "hello world")


if __name__ == "__main__":
    unittest.main()
