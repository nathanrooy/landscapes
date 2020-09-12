import unittest
from math import pi

from landscapes.single_objective import ackley
from landscapes.single_objective import beale
from landscapes.single_objective import booth
from landscapes.single_objective import branin
from landscapes.single_objective import bukin_n6
from landscapes.single_objective import camel_hump_3
from landscapes.single_objective import camel_hump_6
from landscapes.single_objective import cross_in_tray
from landscapes.single_objective import drop_wave
from landscapes.single_objective import easom
from landscapes.single_objective import eggholder
from landscapes.single_objective import goldstein_price
from landscapes.single_objective import griewank
from landscapes.single_objective import himmelblau
from landscapes.single_objective import holder_table
from landscapes.single_objective import levi_n13
from landscapes.single_objective import matyas
from landscapes.single_objective import mccormick
from landscapes.single_objective import rastrigin
from landscapes.single_objective import rotated_hyper_ellipsoid
from landscapes.single_objective import rosenbrock
from landscapes.single_objective import schaffer_n2
from landscapes.single_objective import schaffer_n4
from landscapes.single_objective import schwefel
from landscapes.single_objective import sphere
from landscapes.single_objective import styblinski_tang
from landscapes.single_objective import sum_of_different_powers
from landscapes.single_objective import sum_of_squares
from landscapes.single_objective import trid
from landscapes.single_objective import zakharov

class test_single_objective(unittest.TestCase):

    def test_ackley(self):
        self.assertEqual(ackley([0,0,0]), 0)

    def test_beale(self):
        self.assertEqual(beale([3, 0.5]), 0)

    def test_booth(self):
        self.assertEqual(booth([1,3]), 0)

    def test_branin_1(self):
        self.assertLess(abs(0.397887 - branin([-pi, 12.275])), 1e-6)

    def test_branin_2(self):
        self.assertLess(abs(0.397887 - branin([pi, 2.275])), 1e-6)

    def test_branin_3(self):
        self.assertLess(abs(0.397887 - branin([3*pi, 2.475])), 1e-6)

    def test_bukin_n6(self):
        self.assertEqual(bukin_n6([-10,1]), 0)

    def test_camel_hump_3(self):
        self.assertEqual(camel_hump_3([0,0]), 0)

    def test_camel_hump_6(self):
        self.assertLess(abs(-1.0316 - camel_hump_6([ 0.0898, -0.7126])), 1e-4)
        self.assertLess(abs(-1.0316 - camel_hump_6([-0.0898,  0.7126])), 1e-4)

    def test_cross_in_tray(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([ 1.34941,  1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([ 1.34941, -1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941,  1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941, -1.34941])), 1e-5)

    def test_drop_wave(self):
        self.assertEqual(drop_wave([0,0]), -1)

    def test_easom(self):
        self.assertEqual(easom([pi, pi]), -1)

    def test_eggholder(self):
        self.assertLess(abs(-959.6407 - eggholder([512, 404.2319])), 1e-4)

    def test_goldstein_price(self):
        self.assertEqual(goldstein_price([0,-1]), 3)

    def test_griewank(self):
        self.assertEqual(griewank([0]), 0)
        self.assertEqual(griewank([0,0,0,0,0]), 0)

    def test_himmelblau_1(self):
        self.assertEqual(himmelblau([3,2]), 0)

    def test_himmelblau_2(self):
        self.assertLess(himmelblau([-2.805118, 3.131312]), 1e-10)

    def test_himmelblau_3(self):
        self.assertLess(himmelblau([-3.779310, -3.283186]), 1e-10)

    def test_himmelblau_4(self):
        self.assertLess(himmelblau([3.584428, -1.848126]), 1e-10)

    def test_holder_table_1(self):
        self.assertLess(abs(-19.2085 - holder_table([ 8.05502,  9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([-8.05502,  9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([ 8.05502, -9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([-8.05502, -9.66459])), 1e-5)

    def test_levi_n13(self):
        self.assertLess(levi_n13([1,1]), 1e-10)

    def test_matyas(self):
        self.assertEqual(matyas([0,0]), 0)

    def test_mccormick(self):
        self.assertLess(abs(-1.9133 - mccormick([-0.54719, -1.54719])), 1e-4)

    def test_rastrigin_1(self):
        self.assertEqual(rastrigin([0]), 0)
        self.assertEqual(rastrigin([0,0,0,0,0]), 0)

    def test_rotated_hyper_ellipsoid(self):
        self.assertEqual(rotated_hyper_ellipsoid([0]), 0)
        self.assertEqual(rotated_hyper_ellipsoid([0,0,0,0,0]), 0)

    def test_rosenbrock_1(self):
        self.assertEqual(rosenbrock([1]), 0)
        self.assertEqual(rosenbrock([1,1,1,1,1]), 0)

    def test_schaffer_n2(self):
        self.assertEqual(schaffer_n2([0,0]), 0)

    def test_schaffer_n4_1(self):
        self.assertLess(abs(0.292579 - schaffer_n4([0,  1.25313])), 1e-6)
        self.assertLess(abs(0.292579 - schaffer_n4([0, -1.25313])), 1e-6)

    def test_schwefel_1(self):
        self.assertLess(schwefel([420.9687]), 1e-4)

    def test_schwefel_2(self):
        self.assertLess(schwefel([420.9687, 420.9687, 420.9687, 420.9687, 420.9687]), 1e-4)

    def test_sphere_1(self):
        self.assertEqual(sphere([0]), 0)
        self.assertEqual(sphere([0,0,0,0,0]), 0)

    def test_styblinski_tang_1(self):
        self.assertTrue(-39.16617 <= styblinski_tang([-2.903534]) <= -39.16616)

    def test_styblinski_tang_2(self):
        self.assertTrue(
        -39.16617*5 <=
        styblinski_tang([-2.903534, -2.903534, -2.903534, -2.903534, -2.903534])
        <= -39.16616 * 5
        )

    def test_sum_of_different_powers_1(self):
        self.assertEqual(sum_of_different_powers([0]), 0)
        self.assertEqual(sum_of_different_powers([0,0,0,0,0]), 0)

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([0]), 0)
        self.assertEqual(sum_of_squares([0,0,0,0,0]), 0)

    def test_trid(self):
        # dimensions = 1
        d = 1
        x = [i*(d+1-i) for i in range(1, d+1)]
        sol = -d*(d+4)*(d-1)/6.0
        self.assertEqual(trid(x), sol)

        # dimensions = 5
        d = 5
        x = [i*(d+1.0-i) for i in range(1, d+1)]
        sol = -d*(d+4.0)*(d-1)/6.0
        self.assertEqual(trid(x), sol)

    def test_zakharov(self):
        self.assertEqual(zakharov([0]), 0)
        self.assertEqual(zakharov([0,0,0,0,0]), 0)


if __name__ == '__main__':
    unittest.main()