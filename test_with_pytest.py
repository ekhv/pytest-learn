import os
import unittest


class TestCase(unittest.TestCase):

    def test_always_passes(self):
        """Test True"""
        self.assertTrue(True)

    def test_env_sever(self):
        """Env contains a server name"""
        self.assertIsNotNone(os.environ['app_server'])

    def test_always_fails(self):
        """Test False"""
        self.assertTrue(False)


class TestWorkPiece(unittest.TestCase):
    def test_(self):
        pass


if __name__ == "__main__":
    unittest.main()
