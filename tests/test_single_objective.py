import unittest
from math import pi, sqrt

from landscapes._utils import safe_division
from landscapes.single_objective import (
    ackley,
    ackley_n2,
    adjiman,
    amgm,
    bartels_conn,
    beale,
    bent_cigar,
    bird,
    bohachevsky_n1,
    bohachevsky_n2,
    bohachevsky_n3,
    booth,
    branin,
    brent,
    brown,
    bukin_n6,
    camel_hump_3,
    camel_hump_6,
    carrom_table,
    chichinadze,
    chung_reynolds,
    colville,
    cosine_mixture,
    cross_in_tray,
    csendes,
    cube,
    damavandi,
    deckkers_aarts,
    dixon_price,
    drop_wave,
    easom,
    eggholder,
    exponential,
    freudenstein_roth,
    goldstein_price,
    griewank,
    himmelblau,
    holder_table,
    hosaki,
    keane,
    leon,
    levi_n13,
    matyas,
    mccormick,
    michalewicz,
    parsopoulos,
    pen_holder,
    plateau,
    qing,
    quartic,
    rastrigin,
    rosenbrock,
    rotated_hyper_ellipsoid,
    salomon,
    schaffer_n2,
    schaffer_n4,
    schwefel,
    sphere,
    step,
    styblinski_tang,
    sum_of_different_powers,
    sum_of_squares,
    trid,
    tripod,
    tsp,
    wolfe,
    zakharov,
)

D_MIN = 1
D_MAX = 20


class test_single_objective(unittest.TestCase):
    def test_ackley(self):
        self.assertEqual(ackley(ackley.g_opt[0].x_opt), ackley.g_opt[0].f_opt)

    def test_ackley_n2(self):
        self.assertLess(
            abs(ackley_n2.g_opt[0].f_opt - ackley_n2(ackley_n2.g_opt[0].x_opt)),
            1e-6,
        )

    def test_adjiman(self):
        self.assertLess(
            abs(adjiman.g_opt[0].f_opt - adjiman(adjiman.g_opt[0].x_opt)),
            1e-6,
        )

    def test_amgm(self):
        self.assertEqual(amgm(amgm.g_opt[0].x_opt * 3), amgm.g_opt[0].f_opt)
        self.assertEqual(amgm([1.5, 1.5, 1.5]), amgm.g_opt[0].f_opt)
        self.assertEqual(amgm([1, 1, 1]), amgm.g_opt[0].f_opt)
        self.assertNotEqual(amgm([1, 2, 3, 4, 5, 6, 7]), amgm.g_opt[0].f_opt)

    def test_bartels_conn(self):
        self.assertEqual(
            bartels_conn(bartels_conn.g_opt[0].x_opt),
            bartels_conn.g_opt[0].f_opt,
        )

    def test_beale(self):
        self.assertEqual(beale(beale.g_opt[0].x_opt), beale.g_opt[0].f_opt)

    def test_bent_cigar(self):
        for d in range(D_MIN, D_MAX):
            x = bent_cigar.g_opt[0].x_opt * d
            self.assertEqual(bent_cigar(x), bent_cigar.g_opt[0].f_opt)

    def test_bird(self):
        for opt in bird.g_opt:
            self.assertLess(abs(opt.f_opt - bird(opt.x_opt)), 1e-6)

    def test_bohachevsky_n1(self):
        self.assertEqual(
            bohachevsky_n1(bohachevsky_n1.g_opt[0].x_opt),
            bohachevsky_n1.g_opt[0].f_opt,
        )

    def test_bohachevsky_n2(self):
        self.assertEqual(
            bohachevsky_n2(bohachevsky_n2.g_opt[0].x_opt),
            bohachevsky_n2.g_opt[0].f_opt,
        )

    def test_bohachevsky_n3(self):
        self.assertEqual(
            bohachevsky_n3(bohachevsky_n3.g_opt[0].x_opt),
            bohachevsky_n3.g_opt[0].f_opt,
        )

    def test_booth(self):
        self.assertEqual(booth(booth.g_opt[0].x_opt), booth.g_opt[0].f_opt)

    def test_branin(self):
        for opt in branin.g_opt:
            self.assertLess(abs(opt.f_opt - branin(opt.x_opt)), 1e-6)

    def test_brent(self):
        self.assertLess(abs(brent.g_opt[0].f_opt - brent(brent.g_opt[0].x_opt)), 1e-6)

    def test_brown(self):
        for d in range(D_MIN, D_MAX + 1):
            x = brown.g_opt[0].x_opt * d
            self.assertEqual(abs(brown(x)), brown.g_opt[0].f_opt)

    def test_bukin_n6(self):
        self.assertEqual(bukin_n6(bukin_n6.g_opt[0].x_opt), bukin_n6.g_opt[0].f_opt)

    def test_camel_hump_3(self):
        self.assertEqual(
            camel_hump_3(camel_hump_3.g_opt[0].x_opt),
            camel_hump_3.g_opt[0].f_opt,
        )

    def test_camel_hump_6(self):
        for opt in camel_hump_6.g_opt:
            self.assertLess(
                abs(opt.f_opt - camel_hump_6(opt.x_opt)),
                1e-4,
            )

    def test_carrom_table(self):
        for opt in carrom_table.g_opt:
            self.assertLess(
                abs(opt.f_opt - carrom_table(opt.x_opt)),
                1e-6,
            )

    def test_chichinadze(self):
        self.assertLess(
            abs(chichinadze.g_opt[0].f_opt - chichinadze(chichinadze.g_opt[0].x_opt)),
            1e-6,
        )

    def test_chung_reynolds(self):
        for d in range(D_MIN, D_MAX + 1):
            x = chung_reynolds.g_opt[0].x_opt * d
            self.assertEqual(chung_reynolds(x), chung_reynolds.g_opt[0].f_opt)

    def test_colville(self):
        self.assertEqual(colville(colville.g_opt[0].x_opt), colville.g_opt[0].f_opt)

    def test_cosine_mixture(self):
        for d in range(D_MIN, D_MAX):
            g_min = cosine_mixture.g_opt[0].f_opt * d
            x = cosine_mixture.g_opt[0].x_opt * d
            self.assertLess(abs(g_min - cosine_mixture(x)), 1e-6)

    def test_cross_in_tray(self):
        for opt in cross_in_tray.g_opt:
            self.assertLess(
                abs(opt.f_opt - cross_in_tray(opt.x_opt)),
                1e-5,
            )

    def test_csendes(self):
        for d in range(D_MIN, D_MAX):
            x = csendes.g_opt[0].x_opt * d
            self.assertEqual(csendes(x), csendes.g_opt[0].f_opt)

    def test_cube(self):
        self.assertEqual(cube(cube.g_opt[0].x_opt), cube.g_opt[0].f_opt)

    def test_damavandi(self):
        self.assertEqual(
            damavandi(damavandi.g_opt[0].x_opt),
            damavandi.g_opt[0].f_opt,
        )

    def test_deckkers_aarts(self):
        for opt in deckkers_aarts.g_opt:
            self.assertLess(
                abs(opt.f_opt - deckkers_aarts(opt.x_opt)),
                1e-5,
            )

    def test_dixon_price(self):
        self.assertLess(
            abs(dixon_price(dixon_price.g_opt[0].x_opt) - dixon_price.g_opt[0].f_opt),
            1e-6,
        )
        for d in range(D_MIN, D_MAX + 1):
            g_min = [2 ** (-((2**i) - 2) / 2.0**i) for i in range(1, d + 1)]
            self.assertLess(abs(dixon_price(g_min) - dixon_price.g_opt[0].f_opt), 1e-6)

    def test_drop_wave(self):
        self.assertEqual(drop_wave(drop_wave.g_opt[0].x_opt), drop_wave.g_opt[0].f_opt)

    def test_easom(self):
        self.assertEqual(easom(easom.g_opt[0].x_opt), easom.g_opt[0].f_opt)

    def test_eggholder(self):
        self.assertLess(
            abs(eggholder.g_opt[0].f_opt - eggholder(eggholder.g_opt[0].x_opt)),
            1e-4,
        )

    def test_exponential(self):
        for d in range(D_MIN, D_MAX + 1):
            x = exponential.g_opt[0].x_opt * d
            self.assertEqual(exponential(x), exponential.g_opt[0].f_opt)

    def test_freudenstein_roth(self):
        self.assertEqual(
            freudenstein_roth(freudenstein_roth.g_opt[0].x_opt),
            freudenstein_roth.g_opt[0].f_opt,
        )

    def test_goldstein_price(self):
        self.assertEqual(
            goldstein_price(goldstein_price.g_opt[0].x_opt),
            goldstein_price.g_opt[0].f_opt,
        )

    def test_griewank(self):
        self.assertEqual(griewank(griewank.g_opt[0].x_opt), griewank.g_opt[0].f_opt)
        self.assertEqual(
            griewank(griewank.g_opt[0].x_opt * 5),
            griewank.g_opt[0].f_opt,
        )

    def test_himmelblau_1(self):
        for opt in himmelblau.g_opt:
            self.assertLess(
                abs(opt.f_opt - himmelblau(opt.x_opt)),
                1e-10,
            )

    def test_holder_table_1(self):
        for opt in holder_table.g_opt:
            self.assertLess(
                abs(opt.f_opt - holder_table(opt.x_opt)),
                1e-5,
            )

    def test_hosaki(self):
        self.assertLess(
            abs(hosaki.g_opt[0].f_opt - hosaki(hosaki.g_opt[0].x_opt)),
            1e-5,
        )

    def test_keane(self):
        for opt in keane.g_opt:
            self.assertLess(abs(opt.f_opt - keane(opt.x_opt)), 1e-6)

    def test_levi_n13(self):
        self.assertLess(
            abs(levi_n13(levi_n13.g_opt[0].x_opt) - levi_n13.g_opt[0].f_opt),
            1e-10,
        )

    def test_leon(self):
        self.assertEqual(leon(leon.g_opt[0].x_opt), leon.g_opt[0].f_opt)

    def test_matyas(self):
        self.assertEqual(matyas(matyas.g_opt[0].x_opt), matyas.g_opt[0].f_opt)

    def test_michalewicz(self):
        self.assertTrue(
            michalewicz(michalewicz.g_opt[0].x_opt) >= michalewicz.g_opt[0].f_opt
        )

    def test_mccormick(self):
        self.assertLess(
            abs(mccormick.g_opt[0].f_opt - mccormick(mccormick.g_opt[0].x_opt)),
            1e-4,
        )

    def test_parsopoulos(self):
        self.assertLess(
            abs(parsopoulos(parsopoulos.g_opt[0].x_opt) - parsopoulos.g_opt[0].f_opt),
            1e-6,
        )
        for k in [-1, 1, -3, 3]:
            for m in [0, -1, 1, -2, 2]:
                self.assertLess(
                    abs(parsopoulos([k * pi / 2, m * pi]) - parsopoulos.g_opt[0].f_opt),
                    1e-6,
                )

    def test_pen_holder(self):
        for opt in pen_holder.g_opt:
            self.assertLess(
                abs(opt.f_opt - pen_holder(opt.x_opt)),
                1e-6,
            )

    def test_plateau(self):
        for d in range(D_MIN, D_MAX + 1):
            x = plateau.g_opt[0].x_opt * d
            self.assertEqual(plateau(x), plateau.g_opt[0].f_opt)

    def test_qing(self):
        self.assertLess(abs(qing(qing.g_opt[0].x_opt) - qing.g_opt[0].f_opt), 1e-6)
        for d in range(1, D_MAX + 1):
            self.assertLess(
                abs(qing([sqrt(i) for i in range(1, d + 1)]) - qing.g_opt[0].f_opt),
                1e-6,
            )

    def test_quartic(self):
        for d in range(D_MIN, D_MAX + 1):
            x = quartic.g_opt[0].x_opt * d
            self.assertEqual(quartic(x), quartic.g_opt[0].f_opt)

    def test_rastrigin_1(self):
        self.assertEqual(
            rastrigin(rastrigin.g_opt[0].x_opt),
            rastrigin.g_opt[0].f_opt,
        )
        self.assertEqual(
            rastrigin(rastrigin.g_opt[0].x_opt * 5),
            rastrigin.g_opt[0].f_opt,
        )

    def test_rastrigin_safe_mode(self):
        self.assertEqual(
            rastrigin(rastrigin.g_opt[0].x_opt * 2, safe_mode=True),
            rastrigin.g_opt[0].f_opt,
        )
        with self.assertRaises(AssertionError):
            rastrigin([10.0, 0.0], safe_mode=True)

    def test_rotated_hyper_ellipsoid(self):
        self.assertEqual(
            rotated_hyper_ellipsoid(rotated_hyper_ellipsoid.g_opt[0].x_opt),
            rotated_hyper_ellipsoid.g_opt[0].f_opt,
        )
        self.assertEqual(
            rotated_hyper_ellipsoid(rotated_hyper_ellipsoid.g_opt[0].x_opt * 5),
            rotated_hyper_ellipsoid.g_opt[0].f_opt,
        )

    def test_rosenbrock_1(self):
        self.assertEqual(
            rosenbrock(rosenbrock.g_opt[0].x_opt),
            rosenbrock.g_opt[0].f_opt,
        )
        self.assertEqual(
            rosenbrock(rosenbrock.g_opt[0].x_opt * 5),
            rosenbrock.g_opt[0].f_opt,
        )

    def test_salomon(self):
        for d in range(D_MIN, D_MAX + 1):
            x = salomon.g_opt[0].x_opt * d
            self.assertLess(abs(salomon(x) - salomon.g_opt[0].f_opt), 1e-6)

    def test_schaffer_n2(self):
        self.assertEqual(
            schaffer_n2(schaffer_n2.g_opt[0].x_opt),
            schaffer_n2.g_opt[0].f_opt,
        )

    def test_schaffer_n4_1(self):
        for opt in schaffer_n4.g_opt:
            self.assertLess(
                abs(opt.f_opt - schaffer_n4(opt.x_opt)),
                1e-6,
            )

    def test_schwefel(self):
        for d in range(D_MIN, 7):
            x = schwefel.g_opt[0].x_opt * d
            self.assertLess(abs(schwefel(x) - schwefel.g_opt[0].f_opt), 1e-4)

    def test_sphere(self):
        self.assertEqual(sphere(sphere.g_opt[0].x_opt), sphere.g_opt[0].f_opt)
        self.assertEqual(sphere(sphere.g_opt[0].x_opt * 5), sphere.g_opt[0].f_opt)

    def test_step(self):
        for d in range(D_MIN, D_MAX + 1):
            x = step.g_opt[0].x_opt * d
            self.assertEqual(step(x), step.g_opt[0].f_opt)

    def test_styblinski_tang_1(self):
        val_1d = styblinski_tang(styblinski_tang.g_opt[0].x_opt)
        self.assertAlmostEqual(val_1d, styblinski_tang.g_opt[0].f_opt, places=4)
        val_5d = styblinski_tang(styblinski_tang.g_opt[0].x_opt * 5)
        self.assertAlmostEqual(val_5d, styblinski_tang.g_opt[0].f_opt * 5, places=4)

    def test_sum_of_different_powers_1(self):
        self.assertEqual(
            sum_of_different_powers(sum_of_different_powers.g_opt[0].x_opt),
            sum_of_different_powers.g_opt[0].f_opt,
        )
        self.assertEqual(
            sum_of_different_powers(sum_of_different_powers.g_opt[0].x_opt * 5),
            sum_of_different_powers.g_opt[0].f_opt,
        )

    def test_sum_of_squares(self):
        self.assertEqual(
            sum_of_squares(sum_of_squares.g_opt[0].x_opt),
            sum_of_squares.g_opt[0].f_opt,
        )
        self.assertEqual(
            sum_of_squares(sum_of_squares.g_opt[0].x_opt * 5),
            sum_of_squares.g_opt[0].f_opt,
        )

    def test_trid(self):
        # 1D matches g_opt
        self.assertEqual(trid(trid.g_opt[0].x_opt), trid.g_opt[0].f_opt)
        for d in [1, 5]:
            x = [i * (d + 1.0 - i) for i in range(1, d + 1)]
            sol = -d * (d + 4.0) * (d - 1) / 6.0
            self.assertEqual(trid(x), sol)

    def test_tripod(self):
        self.assertEqual(tripod(tripod.g_opt[0].x_opt), tripod.g_opt[0].f_opt)

    def test_wolfe(self):
        self.assertEqual(wolfe(wolfe.g_opt[0].x_opt), wolfe.g_opt[0].f_opt)

    def test_zakharov(self):
        self.assertEqual(zakharov(zakharov.g_opt[0].x_opt), zakharov.g_opt[0].f_opt)
        self.assertEqual(
            zakharov(zakharov.g_opt[0].x_opt * 5),
            zakharov.g_opt[0].f_opt,
        )

    def test_tsp(self):
        def euclidean_dist(p1, p2):
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
        tsp_closed = tsp(euclidean_dist, close_loop=True)
        tsp_open = tsp(euclidean_dist, close_loop=False)
        self.assertAlmostEqual(tsp_closed.dist(pts), 4.0)
        self.assertAlmostEqual(tsp_open.dist(pts), 3.0)

    def test_utils_safe_division(self):
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(10, 0), 0.0)
        self.assertEqual(safe_division(10, 0.0), 0.0)


if __name__ == "__main__":
    unittest.main()
