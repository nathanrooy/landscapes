import unittest

from math import pi

from landscapes.single_objective import ackley
from landscapes.single_objective import beale
from landscapes.single_objective import booth
from landscapes.single_objective import branin
from landscapes.single_objective import bukin_n6
from landscapes.single_objective import cross_in_tray
from landscapes.single_objective import drop_wave
from landscapes.single_objective import easom
from landscapes.single_objective import eggholder
from landscapes.single_objective import goldstein_price

from landscapes.single_objective import sphere

class test_single_objective(unittest.TestCase):

    def test_ackley(self):
        self.assertEqual(ackley([0,0,0]), 0)

    def test_beale(self):
        self.assertEqual(beale([3, 0.5]), 0)

    def test_booth(self):
        self.assertEqual(booth([1,3]), 0)

    # def test_branin(self):
    #     self.assertEqual(branin([-pi, y=12.275]), 0)

    def test_bukin_n6(self):
        self.assertEqual(bukin_n6([-10,1]), 0)

    def test_cross_in_tray_1(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([1.34941, 1.34941])), 1e-5)

    def test_cross_in_tray_2(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([1.34941, -1.34941])), 1e-5)

    def test_cross_in_tray_3(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941, 1.34941])), 1e-5)

    def test_cross_in_tray_4(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941, -1.34941])), 1e-5)

    def test_drop_wave(self):
        self.assertEqual(drop_wave([0,0]), -1)

    def test_easom(self):
        self.assertEqual(easom([pi, pi]), -1)

    def test_eggholder(self):
        self.assertLess(abs(-959.6407 - eggholder([512, 404.2319])), 1e-4)

    def test_goldstein_price(self):
        self.assertEqual(goldstein_price([0,-1]), 3)

    def test_sphere(self):
        self.assertEqual(sphere([0,0,0]), 0)


if __name__ == '__main__':
    unittest.main()
