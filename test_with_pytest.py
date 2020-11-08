import os
import unittest


class TestCaseOne(unittest.TestCase):
    def test_env_sever(self):
        """Env contains a server name"""
        self.assertIsNotNone(os.environ['app_server'])

@unittest.skip("In progress")
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
