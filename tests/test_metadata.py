import inspect
import unittest
from dataclasses import FrozenInstanceError

import landscapes
import landscapes.single_objective as so
from landscapes._metadata import BenchmarkFunction, Solution, benchmark
from landscapes._references import REFERENCES
from landscapes.single_objective import sphere


class TestMetadata(unittest.TestCase):
    def test_solution_immutability(self) -> None:
        sol = Solution(f_opt=0.0, x_opt=[0.0])
        with self.assertRaises(FrozenInstanceError):
            sol.f_opt = 10.0  # type: ignore[misc]

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
        # get all single objective functions
        so_funcs = [
            (name, obj)
            for name, obj in inspect.getmembers(so, inspect.isfunction)
            if obj.__module__ == so.__name__
            and not name.startswith("_")
            and name != "safe_div"
        ]
        self.assertEqual(len(so_funcs), 66)

        # cycle through each single objective function
        for name, fn in so_funcs:
            with self.subTest(function=name):
                # verify bounds
                self.assertIsInstance(fn.bounds, list)
                self.assertGreaterEqual(len(fn.bounds), 1)
                for b in fn.bounds:
                    self.assertEqual(len(b), 2)
                    self.assertIsInstance(b, tuple)
                    self.assertIsInstance(b[0], (int, float))
                    self.assertIsInstance(b[1], (int, float))

                    # verify lower/upper bound ordering
                    self.assertLessEqual(b[0], b[1])

                # verify dimensions
                self.assertTrue(fn.dimensions is None or isinstance(fn.dimensions, int))

                # verify global optima
                self.assertIsInstance(fn.g_opt, list)
                self.assertGreaterEqual(len(fn.g_opt), 1)
                for opt in fn.g_opt:
                    self.assertIsInstance(opt, Solution)
                    self.assertIsInstance(opt.f_opt, (int, float))
                    self.assertIsInstance(opt.x_opt, list)

                # verify dimensions and bounds sizing
                if fn.dimensions is not None:
                    self.assertEqual(len(fn.bounds), fn.dimensions)
                    for opt in fn.g_opt:
                        self.assertEqual(len(opt.x_opt), fn.dimensions)
                else:
                    self.assertEqual(len(fn.bounds), 1)
                    self.assertEqual(len(fn.bounds * 3), 3)

                # verify docstring has non-empty title and structure
                doc = fn.__doc__ or ""
                self.assertTrue(doc.strip())
                self.assertIn("Benchmark Metadata", doc)
                self.assertIn("Bounds:", doc)
                self.assertIn("Dimensions:", doc)
                self.assertIn("Global Optima:", doc)
                self.assertIn("References\n----------", doc)

                # verify references
                self.assertTrue(hasattr(fn, "_ref"))
                self.assertIsInstance(fn._ref, list)
                self.assertGreaterEqual(len(fn._ref), 1)
                for ref_key in fn._ref:
                    self.assertIn(ref_key, REFERENCES)
                    self.assertIn(REFERENCES[ref_key], doc)


if __name__ == "__main__":
    unittest.main()
