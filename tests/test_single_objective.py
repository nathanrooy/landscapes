import unittest
from math import pi
from math import sqrt

from landscapes.single_objective import ackley
from landscapes.single_objective import ackley_n2
from landscapes.single_objective import adjiman
from landscapes.single_objective import amgm
from landscapes.single_objective import bartels_conn
from landscapes.single_objective import beale
from landscapes.single_objective import bent_cigar
from landscapes.single_objective import bird
from landscapes.single_objective import bohachevsky_n1
from landscapes.single_objective import bohachevsky_n2
from landscapes.single_objective import bohachevsky_n3
from landscapes.single_objective import booth
from landscapes.single_objective import branin
from landscapes.single_objective import brent
from landscapes.single_objective import brown
from landscapes.single_objective import bukin_n6
from landscapes.single_objective import camel_hump_3
from landscapes.single_objective import camel_hump_6
from landscapes.single_objective import carrom_table
from landscapes.single_objective import chichinadze
from landscapes.single_objective import chung_reynolds
from landscapes.single_objective import colville
from landscapes.single_objective import cosine_mixture
from landscapes.single_objective import cross_in_tray
from landscapes.single_objective import csendes
from landscapes.single_objective import cube
from landscapes.single_objective import damavandi
from landscapes.single_objective import deckkers_aarts
from landscapes.single_objective import dixon_price
from landscapes.single_objective import drop_wave
from landscapes.single_objective import easom
from landscapes.single_objective import eggholder
from landscapes.single_objective import exponential
from landscapes.single_objective import freudenstein_roth
from landscapes.single_objective import goldstein_price
from landscapes.single_objective import griewank
from landscapes.single_objective import himmelblau
from landscapes.single_objective import holder_table
from landscapes.single_objective import hosaki
from landscapes.single_objective import keane
from landscapes.single_objective import levi_n13
from landscapes.single_objective import leon
from landscapes.single_objective import matyas
from landscapes.single_objective import michalewicz
from landscapes.single_objective import mccormick
from landscapes.single_objective import parsopoulos
from landscapes.single_objective import pen_holder
from landscapes.single_objective import plateau
from landscapes.single_objective import qing
from landscapes.single_objective import quartic
from landscapes.single_objective import rastrigin
from landscapes.single_objective import rotated_hyper_ellipsoid
from landscapes.single_objective import rosenbrock
from landscapes.single_objective import salomon
from landscapes.single_objective import schaffer_n2
from landscapes.single_objective import schaffer_n4
from landscapes.single_objective import schwefel
from landscapes.single_objective import sphere
from landscapes.single_objective import step
from landscapes.single_objective import styblinski_tang
from landscapes.single_objective import sum_of_different_powers
from landscapes.single_objective import sum_of_squares
from landscapes.single_objective import trid
from landscapes.single_objective import tripod
from landscapes.single_objective import wolfe
from landscapes.single_objective import zakharov

D_MIN = 1
D_MAX = 20

class test_single_objective(unittest.TestCase):

    def test_ackley(self):
        self.assertEqual(ackley([0,0]), 0)

    def test_ackley_n2(self):
        self.assertLess(abs(-200 - ackley_n2([0,0])), 1e-6)

    def test_adjiman(self):
        self.assertLess(abs(-2.02180678 - adjiman([2.0, 0.10578])), 1e-6)

    def test_amgm(self):
        self.assertEqual(amgm([1,1,1]), 0)
        self.assertEqual(amgm([1.5,1.5,1.5]), 0)
        self.assertEqual(amgm([0, 0, 0]), 0)
        self.assertNotEqual(amgm([1,2,3,4,5,6,7]), 0)

    def test_bartels_conn(self):
        self.assertEqual(bartels_conn([0,0]), 1)

    def test_beale(self):
        self.assertEqual(beale([3, 0.5]), 0)

    def test_bent_cigar(self):
        for d in range(D_MIN, D_MAX, 1):
            x = [0 for i in range(0, d)]
            self.assertEqual(bent_cigar(x), 0)

    def test_bird(self):
        self.assertLess(abs(-106.764536 - bird([ 4.701055,  3.152946])), 1e-6)
        self.assertLess(abs(-106.764536 - bird([-1.582142, -3.130246])), 1e-6)

    def test_bohachevsky_n1(self):
        self.assertEqual(abs(bohachevsky_n1([0,0])), 0)

    def test_bohachevsky_n2(self):
        self.assertEqual(abs(bohachevsky_n2([0,0])), 0)

    def test_bohachevsky_n3(self):
        self.assertEqual(abs(bohachevsky_n3([0,0])), 0)

    def test_booth(self):
        self.assertEqual(booth([1,3]), 0)

    def test_branin(self):
        self.assertLess(abs(0.397887 - branin([ -pi, 12.275])), 1e-6)
        self.assertLess(abs(0.397887 - branin([  pi,  2.275])), 1e-6)
        self.assertLess(abs(0.397887 - branin([3*pi,  2.475])), 1e-6)

    def test_brent(self):
        self.assertLess(abs(brent([-10, -10])), 1e-6)

    def test_brown(self):
        for d in range(D_MIN, D_MAX + 1):
            self.assertEqual(abs(brown([0 for i in range(0, d)])), 0)

    def test_bukin_n6(self):
        self.assertEqual(bukin_n6([-10,1]), 0)

    def test_camel_hump_3(self):
        self.assertEqual(camel_hump_3([0,0]), 0)

    def test_camel_hump_6(self):
        self.assertLess(abs(-1.0316 - camel_hump_6([ 0.0898, -0.7126])), 1e-4)
        self.assertLess(abs(-1.0316 - camel_hump_6([-0.0898,  0.7126])), 1e-4)

    def test_carrom_table(self):
        self.assertLess(abs(-24.1568155 -carrom_table([ 9.6461572,  9.6461572])), 1e-6)
        self.assertLess(abs(-24.1568155 -carrom_table([ 9.6461572, -9.6461572])), 1e-6)
        self.assertLess(abs(-24.1568155 -carrom_table([-9.6461572,  9.6461572])), 1e-6)
        self.assertLess(abs(-24.1568155 -carrom_table([-9.6461572, -9.6461572])), 1e-6)

    def test_chichinadze(self):
        self.assertLess(abs(-42.9443870 - chichinadze([6.189866586965680, 0.5])), 1e-6)

    def test_chung_reynolds(self):
        for d in range(D_MIN, D_MAX+1, 1):
            x = [0 for i in range(0, d)]
            self.assertEqual(chung_reynolds(x), 0)

    def test_colville(self):
        self.assertEqual(colville([1,1,1,1]), 0)

    def test_cosine_mixture(self):
        for d in range(D_MIN, D_MAX, 1):
            g_min = -0.1 * d
            x = [0 for i in range(0, d)]
            self.assertLess(abs(g_min - cosine_mixture(x)), 1e-6)

    def test_cross_in_tray(self):
        self.assertLess(abs(-2.06261 - cross_in_tray([ 1.34941,  1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([ 1.34941, -1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941,  1.34941])), 1e-5)
        self.assertLess(abs(-2.06261 - cross_in_tray([-1.34941, -1.34941])), 1e-5)

    def test_csendes(self):
        for d in range(D_MIN, D_MAX, 1):
            x = [0 for i in range(0, d)]
            self.assertEqual(csendes(x), 0)

    def test_cube(self):
        self.assertEqual(cube([1,1]), 0)

    def test_damavandi(self):
        self.assertEqual(damavandi([2,2]), 0)

    def test_deckkers_aarts(self):
        self.assertLess(abs(-24771.09375 - deckkers_aarts([0,  15])), 1e-5)
        self.assertLess(abs(-24771.09375 - deckkers_aarts([0, -15])), 1e-5)

    def test_dixon_price(self):
        for d in range(D_MIN, D_MAX + 1):
            g_min = [2**(-(2**i-2)/2.0**i) for i in range(1, d+1)]
            self.assertLess(abs(dixon_price(g_min)), 1e-6)

    def test_drop_wave(self):
        self.assertEqual(drop_wave([0,0]), -1)

    def test_easom(self):
        self.assertEqual(easom([pi, pi]), -1)

    def test_eggholder(self):
        self.assertLess(abs(-959.6407 - eggholder([512, 404.2319])), 1e-4)

    def test_exponential(self):
        for d in range(D_MIN, D_MAX + 1):
            self.assertEqual(exponential([0 for _ in range(1, d+1)]), -1)

    def test_freudenstein_roth(self):
        self.assertEqual(freudenstein_roth([5,4]), 0)

    def test_goldstein_price(self):
        self.assertEqual(goldstein_price([0,-1]), 3)

    def test_griewank(self):
        self.assertEqual(griewank([0]), 0)
        self.assertEqual(griewank([0,0,0,0,0]), 0)

    def test_himmelblau_1(self):
        self.assertEqual(himmelblau([3,2]), 0)
        self.assertLess(himmelblau([-2.805118,  3.131312]), 1e-10)
        self.assertLess(himmelblau([-3.779310, -3.283186]), 1e-10)
        self.assertLess(himmelblau([ 3.584428, -1.848126]), 1e-10)

    def test_holder_table_1(self):
        self.assertLess(abs(-19.2085 - holder_table([ 8.05502,  9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([-8.05502,  9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([ 8.05502, -9.66459])), 1e-5)
        self.assertLess(abs(-19.2085 - holder_table([-8.05502, -9.66459])), 1e-5)

    def test_hosaki(self):
        self.assertLess(abs(-2.345811 - hosaki([4,2])), 1e-5)

    def test_keane(self):
        self.assertLess(abs(0.6736675 - keane([0, 1.3932490])), 1e-6)
        self.assertLess(abs(0.6736675 - keane([1.3932490, 0])), 1e-6)

    def test_levi_n13(self):
        self.assertLess(levi_n13([1,1]), 1e-10)

    def test_leon(self):
        self.assertEqual(leon([1,1]), 0)

    def test_matyas(self):
        self.assertEqual(matyas([0,0]), 0)

    def test_michalewicz(self):
        self.assertTrue( -1.8013 <= michalewicz([2.20,1.57]))

    def test_mccormick(self):
        self.assertLess(abs(-1.9133 - mccormick([-0.54719, -1.54719])), 1e-4)

    def test_parsopoulos(self):
        for k in [-1, 1, -3, 3]:
            for l in [0, -1, 1, -2, 2]:
                self.assertLess(abs(parsopoulos([k*pi/2,  l*pi])), 1e-6)

    def test_pen_holder(self):
        self.assertLess(abs(-0.9635348 - pen_holder([ 9.6461677,  9.6461676])), 1e-6)
        self.assertLess(abs(-0.9635348 - pen_holder([-9.6461677,  9.6461676])), 1e-6)
        self.assertLess(abs(-0.9635348 - pen_holder([ 9.6461677, -9.6461676])), 1e-6)
        self.assertLess(abs(-0.9635348 - pen_holder([-9.6461677, -9.6461676])), 1e-6)

    def test_plateau(self):
        for d in range(D_MIN, D_MAX + 1):
            self.assertEqual(plateau([0 for i in range(0, d)]), 30)

    def test_qing(self):
        for d in range(1, D_MAX +1):
            self.assertLess(qing([sqrt(i) for i in range(1, d+1)]), 1e-6)

    def test_quartic(self):
        for d in range(D_MIN, D_MAX+1, 1):
            x = [0 for i in range(0, d)]
            self.assertEqual(quartic(x), 0)

    def test_rastrigin_1(self):
        self.assertEqual(rastrigin([0]), 0)
        self.assertEqual(rastrigin([0,0,0,0,0]), 0)

    def test_rotated_hyper_ellipsoid(self):
        self.assertEqual(rotated_hyper_ellipsoid([0]), 0)
        self.assertEqual(rotated_hyper_ellipsoid([0,0,0,0,0]), 0)

    def test_rosenbrock_1(self):
        self.assertEqual(rosenbrock([1]), 0)
        self.assertEqual(rosenbrock([1,1,1,1,1]), 0)

    def test_salomon(self):
        for d in range(D_MIN, D_MAX + 1):
            self.assertLess(abs(salomon([0 for i in range(0, d)])), 1e-6)

    def test_schaffer_n2(self):
        self.assertEqual(schaffer_n2([0,0]), 0)

    def test_schaffer_n4_1(self):
        self.assertLess(abs(0.292579 - schaffer_n4([0,  1.25313])), 1e-6)
        self.assertLess(abs(0.292579 - schaffer_n4([0, -1.25313])), 1e-6)

    def test_schwefel(self):
        for d in range(D_MIN, 7):
            self.assertLess(schwefel([420.96874 for i in range(0, d)]), 1e-4)

    def test_sphere(self):
        self.assertEqual(sphere([0]), 0)
        self.assertEqual(sphere([0,0,0,0,0]), 0)

    def test_step(self):
        for d in range(D_MIN, D_MAX + 1):
            self.assertEqual(step([0 for i in range(0, d)]), 0)

    def test_styblinski_tang_1(self):
        self.assertTrue(-39.16617 <= styblinski_tang([-2.903534]) <= -39.16616)
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

    def test_tripod(self):
        self.assertEqual(tripod([0,-50]), 0)

    def test_wolfe(self):
        self.assertEqual(wolfe([0,0,0]), 0)

    def test_zakharov(self):
        self.assertEqual(zakharov([0]), 0)
        self.assertEqual(zakharov([0,0,0,0,0]), 0)


if __name__ == '__main__':
    unittest.main()
