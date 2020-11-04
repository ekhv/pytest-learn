import os
import unittest


class TestCaseOne(unittest.TestCase):
    def test_always_passes(self):
        """Test True"""
        self.assertTrue(True)

    def test_env_sever(self):
        """Env contains a server name"""
        self.assertIsNotNone(os.environ['app_server'])

    def test_always_fails(self):
        """Test False"""
        self.assertTrue(False)


class TestCaseTwo(unittest.TestCase):
    """Work piece"""

    def test_wp_1(self):
        pass

    def test_wp_2(self):
        pass

    def test_wp_3(self):
        pass


if __name__ == "__main__":
    unittest.main()
