import unittest
validUTF8 = __import__('0-validate_utf8').validUTF8


class TestValidUTF8(unittest.TestCase):

    def test_validUTF8(self):
        # test valid UTF-8 sequences
        self.assertTrue(
            validUTF8([0b00100100, 0b01100010, 0b11100010, 0b10000010, 0b10110010]))
        self.assertTrue(validUTF8([0b11100010, 0b10000010, 0b10110010]))
        self.assertTrue(
            validUTF8([0b11110, 0b10000000, 0b10000000, 0b10000000]))

        # test invalid UTF-8 sequences
        # continuation byte without a start byte
        self.assertFalse(validUTF8([0b10000000]))
        # incomplete 2-byte sequence
        self.assertFalse(validUTF8([0b11000000, 0b00000000]))
        # incomplete 3-byte sequence
        self.assertFalse(validUTF8([0b11100000, 0b10000000]))
        # incomplete 4-byte sequence
        self.assertFalse(validUTF8([0b11110000, 0b10000000, 0b10000000]))
        # invalid 5-byte sequence
        self.assertFalse(
            validUTF8([0b11111000, 0b10000000, 0b10000000, 0b10000000]))
        # invalid 6-byte sequence
        self.assertFalse(
            validUTF8([0b11111100, 0b10000000, 0b10000000, 0b10000000, 0b10000000]))
        # overlong 3-byte sequence
        self.assertFalse(validUTF8([0b11100000, 0b10000000, 0b00100000]))
        # overlong 4-byte sequence
        self.assertFalse(
            validUTF8([0b11110000, 0b10000000, 0b10000000, 0b00000001]))
        # surrogate pair
        self.assertFalse(
            validUTF8([0b11110000, 0b10000000, 0b10100000, 0b10000000]))
