import unittest

from landscapes.single_objective import sphere

class test_single_objective(unittest.TestCase):
    def test_sphere(self):
        self.assertEqual(sphere([0,0,0]), 0)

if __name__ == '__main__':
    unittest.main()
