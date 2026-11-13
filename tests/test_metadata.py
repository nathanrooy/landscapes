import inspect
import types
import unittest
from dataclasses import FrozenInstanceError

import landscapes
import landscapes.single_objective as so
from landscapes._metadata import BenchmarkFunction, Solution, benchmark
from landscapes.single_objective import ackley, camel_hump_6, himmelblau, sphere


class TestMetadata(unittest.TestCase):
    def test_metadata_attributes(self) -> None:
        self.assertIsInstance(ackley, types.FunctionType)
        self.assertEqual(ackley.bounds, [(-5.0, 5.0), (-5.0, 5.0)])
        self.assertEqual(ackley.dimensions, 2)
        self.assertEqual(len(ackley.g_opt), 1)

    def test_g_opt_structure(self) -> None:
        # Ackley has 1 global optimum
        self.assertEqual(len(ackley.g_opt), 1)
        opt0 = ackley.g_opt[0]
        self.assertIsInstance(opt0, Solution)

        # test attribute access
        self.assertEqual(opt0.f_opt, 0.0)
        self.assertEqual(opt0.x_opt, [0.0, 0.0])

        # test immutability
        with self.assertRaises(FrozenInstanceError):
            opt0.f_opt = 10.0  # type: ignore[misc]

        # 6-Hump Camel has 2 global optima
        self.assertEqual(len(camel_hump_6.g_opt), 2)
        for opt in camel_hump_6.g_opt:
            self.assertAlmostEqual(opt.f_opt, -1.031628, places=4)
            self.assertEqual(len(opt.x_opt), 2)

        # Himmelblau has 4 global optima
        self.assertEqual(len(himmelblau.g_opt), 4)
        for opt in himmelblau.g_opt:
            self.assertEqual(opt.f_opt, 0.0)
            self.assertEqual(len(opt.x_opt), 2)

    def test_scalable_dimensions(self) -> None:
        self.assertEqual(sphere.bounds, [(-5.12, 5.12)])
        self.assertIsNone(sphere.dimensions)
        self.assertEqual(
            sphere.bounds * 3,
            [(-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12)],
        )

    def test_package_exports(self) -> None:
        self.assertIs(landscapes.benchmark, benchmark)
        self.assertIs(landscapes.BenchmarkFunction, BenchmarkFunction)
        self.assertIs(landscapes.Solution, Solution)

    def test_all_single_objective_functions_have_metadata(self) -> None:
        so_funcs = [
            (name, obj)
            for name, obj in inspect.getmembers(so, inspect.isfunction)
            if obj.__module__ == so.__name__
            and not name.startswith("_")
            and name != "safe_div"
        ]
        self.assertEqual(len(so_funcs), 66)

        for name, fn in so_funcs:
            with self.subTest(function=name):
                # verify bounds
                self.assertIsInstance(fn.bounds, list)
                self.assertGreaterEqual(len(fn.bounds), 1)
                for b in fn.bounds:
                    self.assertIsInstance(b, tuple)
                    self.assertEqual(len(b), 2)
                    self.assertIsInstance(b[0], (int, float))
                    self.assertIsInstance(b[1], (int, float))
                    self.assertLessEqual(b[0], b[1])

                # verify dimensions
                self.assertTrue(fn.dimensions is None or isinstance(fn.dimensions, int))

                # verify global optima
                self.assertIsInstance(fn.g_opt, list)
                self.assertGreaterEqual(len(fn.g_opt), 1)

                # verify dimensions and bounds sizing
                if fn.dimensions is not None:
                    self.assertEqual(len(fn.bounds), fn.dimensions)
                    for opt in fn.g_opt:
                        self.assertIsInstance(opt, Solution)
                        self.assertEqual(len(opt.x_opt), fn.dimensions)
                else:
                    self.assertEqual(len(fn.bounds), 1)
                    self.assertEqual(len(fn.bounds * 3), 3)

                # verify docstring
                doc = fn.__doc__ or ""
                self.assertIn("Benchmark Metadata", doc)
                self.assertIn("Bounds:", doc)
                self.assertIn("Dimensions:", doc)
                self.assertIn("Global Optima:", doc)


if __name__ == "__main__":
    unittest.main()
