#!/usr/bin/env python3

import unittest


class TestCase(unittest.TestCase):

    def test_always_passes(self):
        """Test True"""
        self.assertTrue(True)

    def test_always_fails(self):
        """Test False"""
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
