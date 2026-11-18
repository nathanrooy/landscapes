# ------------------------------------------------------------------------------+
#
#   Nathan A. Rooy and contributors
#   Nov. 2019
#
# ------------------------------------------------------------------------------+

# --- IMPORT DEPENDENCIES ------------------------------------------------------+

from collections.abc import Callable, Sequence
from math import cos, e, exp, floor, pi, prod, sin, sqrt
from typing import Any

from landscapes._metadata import Solution, benchmark
from landscapes._utils import safe_division as safe_div


# --- FUNCTIONS ----------------------------------------------------------------+
@benchmark(
    bounds=[
        (-5.0, 5.0),
        (-5.0, 5.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["wikipedia_ackley"],
)
def ackley(xy: Sequence[float]) -> float:
    """Ackley Function."""
    x, y = xy[0], xy[1]
    return (
        -20 * exp(-0.2 * sqrt(0.5 * (x * x + y * y)))
        - exp(0.5 * (cos(2.0 * pi * x) + cos(2 * pi * y)))
        + e
        + 20
    )


@benchmark(
    bounds=[
        (-32.0, 32.0),
        (-32.0, 32.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-200.0, x_opt=[0.0, 0.0])],
    _ref=["ackley1987"],
)
def ackley_n2(xy: Sequence[float]) -> float:
    """Ackley N.2 Function."""
    x, y = xy[0], xy[1]
    return -200 * exp(-0.02 * sqrt(x**2 + y**2))


@benchmark(
    bounds=[
        (-1.0, 2.0),
        (-1.0, 1.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-2.02180678, x_opt=[2.0, 0.10578])],
    _ref=["adjiman1998"],
)
def adjiman(xy: Sequence[float]) -> float:
    """Adjiman Function."""
    x, y = xy[0], xy[1]
    return (cos(x) * sin(y)) - (x / (y**2 + 1.0))


@benchmark(
    bounds=[(0.0, 10.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["mishra2006"],
)
def amgm(x: Sequence[float]) -> float:
    """AMGM: Arithmetic Mean-Geometric Mean (Mishra's Function No.11).

    An infinite number of global minima exist when all coordinate values are
    non-negative and equal (e.g. f(0, ..., 0) = 0, f(1, ..., 1) = 0).
    """
    assert len(x) >= 2, "len(x) must be >= 2"

    d = len(x)
    a = sum([abs(v) for v in x]) / d
    b = abs(prod(x)) ** (1 / d)
    return float((a - b) ** 2)


@benchmark(
    bounds=[
        (-500.0, 500.0),
        (-500.0, 500.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=1.0, x_opt=[0.0, 0.0])],
    _ref=["jamil2013"],
)
def bartels_conn(xy: Sequence[float]) -> float:
    """Bartels Conn Function."""
    x1, x2 = xy[0], xy[1]
    return abs(x1**2 + x2**2 + x1 * x2) + abs(sin(x1)) + abs(cos(x2))


@benchmark(
    bounds=[
        (-4.5, 4.5),
        (-4.5, 4.5),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[3.0, 0.5])],
    _ref=["wikipedia_test_functions"],
)
def beale(xy: Sequence[float]) -> float:
    """Beale Function."""
    x, y = xy[0], xy[1]
    return (
        (1.500 - x + x * y) ** 2
        + (2.250 - x + x * y**2) ** 2
        + (2.625 - x + x * y**3) ** 2
    )


@benchmark(
    bounds=[(-100.0, 100.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["al_roomi_bent_cigar"],
)
def bent_cigar(x: Sequence[float]) -> float:
    """Bent Cigar Function."""
    return x[0] ** 2 + 1e6 * sum([v**2 for v in x[1:]])


@benchmark(
    bounds=[
        (-2 * pi, 2 * pi),
        (-2 * pi, 2 * pi),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-106.764536, x_opt=[4.701055, 3.152946]),
        Solution(f_opt=-106.764536, x_opt=[-1.582142, -3.130246]),
    ],
    _ref=["mishra2006"],
)
def bird(xy: Sequence[float]) -> float:
    """Bird Function."""
    x, y = xy[0], xy[1]
    return (
        sin(x) * exp((1 - cos(y)) ** 2) + cos(y) * exp((1 - sin(x)) ** 2) + (x - y) ** 2
    )


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["bohachevsky1986"],
)
def bohachevsky_n1(xy: Sequence[float]) -> float:
    """Bohachevsky N.1 Function."""
    x, y = xy[0], xy[1]
    return x**2 + 2 * y**2 - 0.3 * cos(3.0 * pi * x) - 0.4 * cos(4 * pi * y) + 0.7


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["bohachevsky1986"],
)
def bohachevsky_n2(xy: Sequence[float]) -> float:
    """Bohachevsky N.2 Function."""
    x, y = xy[0], xy[1]
    return x**2 + 2 * y**2 - 0.3 * cos(3 * pi * x) * cos(4 * pi * y) + 0.3


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["bohachevsky1986"],
)
def bohachevsky_n3(xy: Sequence[float]) -> float:
    """Bohachevsky N.3 Function."""
    x, y = xy[0], xy[1]
    return x**2 + 2 * y**2 - 0.3 * cos(3 * pi * x + 4 * pi * y) + 0.3


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0, 3.0])],
    _ref=["wikipedia_test_functions"],
)
def booth(xy: Sequence[float]) -> float:
    """Booth Function."""
    x, y = xy[0], xy[1]
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


@benchmark(
    bounds=[
        (-5.0, 10.0),
        (0.0, 15.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=0.397887, x_opt=[-pi, 12.275]),
        Solution(f_opt=0.397887, x_opt=[pi, 2.275]),
        Solution(f_opt=0.397887, x_opt=[9.424778, 2.475]),
    ],
    _ref=["surjanovic_branin"],
)
def branin(xy: Sequence[float]) -> float:
    """Branin Function."""
    a = 1
    b = 5.1 / (4 * pi**2)
    c = 5 / pi
    r = 6
    s = 10
    t = 1 / (8 * pi)
    x, y = xy[0], xy[1]
    return a * (y - b * x**2 + c * x - r) ** 2 + s * (1 - t) * cos(x) + s


@benchmark(
    bounds=[
        (-10.0, 2.0),
        (-10.0, 2.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[-10.0, -10.0])],
    _ref=["mishra2006"],
)
def brent(xy: Sequence[float]) -> float:
    """Brent Function."""
    x, y = xy[0], xy[1]
    return (x + 10.0) ** 2 + (y + 10.0) ** 2 + exp(-(x**2) - y**2)


@benchmark(
    bounds=[(-1.0, 4.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["begambre2009"],
)
def brown(x: Sequence[float]) -> float:
    """Brown Function."""
    return float(
        sum(
            [
                ((x[i] ** 2) ** (x[i + 1] ** 2 + 1.0))
                + ((x[i + 1] ** 2) ** (x[i] ** 2 + 1.0))
                for i in range(len(x) - 1)
            ]
        )
    )


@benchmark(
    bounds=[
        (-15.0, -5.0),
        (-3.0, 3.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[-10.0, 1.0])],
    _ref=["wikipedia_test_functions"],
)
def bukin_n6(xy: Sequence[float]) -> float:
    """Bukin Function N.6."""
    x, y = xy[0], xy[1]
    return 100 * sqrt(abs(y - 0.01 * x**2)) + 0.01 * abs(x + 10)


@benchmark(
    bounds=[
        (-5.0, 5.0),
        (-5.0, 5.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["wikipedia_test_functions"],
)
def camel_hump_3(xy: Sequence[float]) -> float:
    """Three-Hump Camel Function."""
    x, y = xy[0], xy[1]
    return 2.0 * x**2 - 1.05 * x**4 + (x**6 / 6.0) + x * y + y**2


@benchmark(
    bounds=[
        (-3.0, 3.0),
        (-2.0, 2.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-1.031628453489877, x_opt=[0.089842, -0.712656]),
        Solution(f_opt=-1.031628453489877, x_opt=[-0.089842, 0.712656]),
    ],
    _ref=["molga2005"],
)
def camel_hump_6(xy: Sequence[float]) -> float:
    """Six-Hump Camel Function."""
    x, y = xy[0], xy[1]
    a = (4 - (2.1 * x**2) + (x**4) / 3.0) * x**2
    b = x * y
    c = (-4 + (4 * y**2)) * y**2
    return a + b + c


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-24.1568155, x_opt=[9.6461572, 9.6461572]),
        Solution(f_opt=-24.1568155, x_opt=[9.6461572, -9.6461572]),
        Solution(f_opt=-24.1568155, x_opt=[-9.6461572, 9.6461572]),
        Solution(f_opt=-24.1568155, x_opt=[-9.6461572, -9.6461572]),
    ],
    _ref=["mishra2006"],
)
def carrom_table(xy: Sequence[float]) -> float:
    """Carrom Table Function."""
    x, y = xy[0], xy[1]
    return (
        exp(2 * abs(1 - (sqrt(x**2 + y**2) / pi))) * cos(x) ** 2 * cos(y) ** 2
    ) / -30.0


@benchmark(
    bounds=[
        (-30.0, 30.0),
        (-30.0, 30.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-42.944387, x_opt=[6.18986658696568, 0.5])],
    _ref=["wikipedia_test_functions"],
)
def chichinadze(xy: Sequence[float]) -> float:
    """Chichinadze Function."""
    x, y = xy[0], xy[1]
    return (
        x**2
        - 12 * x
        + 11
        + 10 * cos(pi * x / 2)
        + 8 * sin(5 * pi * x / 2)
        - 1.0 / sqrt(5) * exp(-((y - 0.5) ** 2) / 2)
    )


@benchmark(
    bounds=[(-100.0, 100.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["chung1998"],
)
def chung_reynolds(x: Sequence[float]) -> float:
    """Chung Reynolds Function."""
    return sphere(x) ** 2


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=4,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0, 1.0, 1.0, 1.0])],
    _ref=["hedar2005"],
)
def colville(xy: Sequence[float]) -> float:
    """Colville Function."""
    x1, x2, x3, x4 = xy[0], xy[1], xy[2], xy[3]
    a = 100 * (x1**2 - x2) ** 2
    b = (x1 - 1) ** 2
    c = (x3 - 1) ** 2
    d = 90 * (x3**2 - x4) ** 2
    e = 10.1 * ((x2 - 1) ** 2 + (x4 - 1) ** 2)
    f = 19.8 * (x2 - 1) * (x4 - 1)
    return a + b + c + d + e + f


@benchmark(
    bounds=[(-1.0, 1.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=-0.1, x_opt=[0.0])],
    _ref=["ali2005"],
)
def cosine_mixture(x: Sequence[float]) -> float:
    """Cosine Mixture Function."""
    return -0.1 * sum([cos(5 * pi * v) for v in x]) + sum([v**2 for v in x])


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-2.06261, x_opt=[1.34941, 1.34941]),
        Solution(f_opt=-2.06261, x_opt=[1.34941, -1.34941]),
        Solution(f_opt=-2.06261, x_opt=[-1.34941, 1.34941]),
        Solution(f_opt=-2.06261, x_opt=[-1.34941, -1.34941]),
    ],
    _ref=["wikipedia_test_functions"],
)
def cross_in_tray(xy: Sequence[float]) -> float:
    """Cross-in-Tray Function."""
    x, y = xy[0], xy[1]
    return float(
        -0.0001
        * (abs(sin(x) * sin(y) * exp(abs(100 - (sqrt(x**2 + y**2) / pi)))) + 1) ** 0.1
    )


@benchmark(
    bounds=[(-1.0, 1.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["csendes1997"],
)
def csendes(x: Sequence[float]) -> float:
    """Csendes Function."""
    return sum([v**6 * (2 + sin(safe_div(1, v))) for v in x])


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0, 1.0])],
    _ref=["lavi1966"],
)
def cube(xy: Sequence[float]) -> float:
    """Cube Function."""
    x, y = xy[0], xy[1]
    return 100 * (y - x**3) ** 2 + (1 - x) ** 2


@benchmark(
    bounds=[
        (0.0, 14.0),
        (0.0, 14.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[2.0, 2.0])],
    _ref=["damavandi2005"],
)
def damavandi(xy: Sequence[float]) -> float:
    """Damavandi Function."""
    x, y = xy[0], xy[1]
    # division by zero causes errors...
    if x == 2 and y == 2:
        return 0
    n = sin(pi * (x - 2)) * sin(pi * (y - 2))
    d = pi**2 * (x - 2) * (y - 2)
    a = 1.0 - (abs(n / d)) ** 5
    b = 2.0 + (x - 7) ** 2 + 2 * (y - 7) ** 2
    return a * b


@benchmark(
    bounds=[
        (-20.0, 20.0),
        (-20.0, 20.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-24776.5183423, x_opt=[0.0, 14.94511215]),
        Solution(f_opt=-24776.5183423, x_opt=[0.0, -14.94511215]),
    ],
    _ref=["ali2005"],
)
def deckkers_aarts(xy: Sequence[float]) -> float:
    """Deckkers-Aarts Function."""
    x, y = xy[0], xy[1]
    return 10**5 * x**2 + y**2 - (x**2 + y**2) ** 2 + 10 ** (-5) * (x**2 + y**2) ** 4


@benchmark(
    bounds=[(-10.0, 10.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0])],
    _ref=["dixon1989"],
)
def dixon_price(x: Sequence[float]) -> float:
    """Dixon and Price Function."""
    return (x[0] - 1.0) ** 2 + sum(
        [(i + 1) * (2.0 * x[i] ** 2 - x[i - 1]) ** 2 for i in range(1, len(x))]
    )


@benchmark(
    bounds=[
        (-5.12, 5.12),
        (-5.12, 5.12),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-1.0, x_opt=[0.0, 0.0])],
    _ref=["surjanovic_drop_wave"],
)
def drop_wave(xy: Sequence[float]) -> float:
    """Drop-Wave Function."""
    x, y = xy[0], xy[1]
    return -(1 + cos(12 * sqrt(x**2 + y**2))) / (0.5 * (x**2 + y**2) + 2)


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-1.0, x_opt=[pi, pi])],
    _ref=["wikipedia_test_functions"],
)
def easom(xy: Sequence[float]) -> float:
    """Easom Function."""
    x, y = xy[0], xy[1]
    return -cos(x) * cos(y) * exp(-((x - pi) ** 2) - (y - pi) ** 2)


@benchmark(
    bounds=[
        (-512.0, 512.0),
        (-512.0, 512.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-959.6406627, x_opt=[512.0, 404.2319])],
    _ref=["wikipedia_test_functions"],
)
def eggholder(xy: Sequence[float]) -> float:
    """Eggholder Function."""
    x, y = xy[0], xy[1]
    return -(y + 47) * sin(sqrt(abs((x / 2.0) + (y + 47)))) - x * sin(
        sqrt(abs(x - (y + 47)))
    )


@benchmark(
    bounds=[(-1.0, 1.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=-1.0, x_opt=[0.0])],
    _ref=["rahnamayan2007_ode"],
)
def exponential(x: Sequence[float]) -> float:
    """Exponential Function."""
    return -exp(-0.5 * sum([v**2 for v in x]))


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[5.0, 4.0])],
    _ref=["rao2009"],
)
def freudenstein_roth(xy: Sequence[float]) -> float:
    """Freudenstein Roth Function."""
    x, y = xy[0], xy[1]
    a = (x - 13 + ((5 - y) * y - 2) * y) ** 2
    b = (x - 29 + ((y + 1) * y - 14) * y) ** 2
    return a + b


@benchmark(
    bounds=[
        (-2.0, 2.0),
        (-2.0, 2.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=3.0, x_opt=[0.0, -1.0])],
    _ref=["wikipedia_test_functions"],
)
def goldstein_price(xy: Sequence[float]) -> float:
    """Goldstein-Price Function."""
    x, y = xy[0], xy[1]
    return (
        1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2)
    ) * (
        30
        + (2 * x - 3 * y) ** 2
        * (18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2)
    )


@benchmark(
    bounds=[(-600.0, 600.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["griewank1981"],
)
def griewank(xy: Sequence[float]) -> float:
    """Griewank Function."""
    a, b = 0.0, 1.0
    for i, v in enumerate(xy):
        a += v**2 / 4000.0
        b *= cos(v / sqrt(i + 1))
    return a - b + 1


@benchmark(
    bounds=[
        (-5.0, 5.0),
        (-5.0, 5.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=0.0, x_opt=[3.0, 2.0]),
        Solution(f_opt=0.0, x_opt=[-2.805118, 3.131312]),
        Solution(f_opt=0.0, x_opt=[-3.77931, -3.283186]),
        Solution(f_opt=0.0, x_opt=[3.584428, -1.848126]),
    ],
    _ref=["wikipedia_himmelblau"],
)
def himmelblau(xy: Sequence[float]) -> float:
    """Himmelblau's Function."""
    x, y = xy[0], xy[1]
    return (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-19.2085, x_opt=[8.05502, 9.66459]),
        Solution(f_opt=-19.2085, x_opt=[-8.05502, 9.66459]),
        Solution(f_opt=-19.2085, x_opt=[8.05502, -9.66459]),
        Solution(f_opt=-19.2085, x_opt=[-8.05502, -9.66459]),
    ],
    _ref=["wikipedia_test_functions"],
)
def holder_table(xy: Sequence[float]) -> float:
    """Hölder Table Function."""
    x, y = xy[0], xy[1]
    return -abs(sin(x) * cos(y) * exp(abs(1 - (sqrt(x**2 + y**2) / pi))))


@benchmark(
    bounds=[
        (0.0, 5.0),
        (0.0, 6.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-2.345811, x_opt=[4.0, 2.0])],
    _ref=["bekey1974"],
)
def hosaki(xy: Sequence[float]) -> float:
    """Hosaki Function."""
    x, y = xy[0], xy[1]
    return (1 - 8 * x + 7 * x**2 - (7.0 / 3.0) * x**3 + 0.25 * x**4) * y**2 * exp(-y)


@benchmark(
    bounds=[
        (0.0, 10.0),
        (0.0, 10.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-0.6736675, x_opt=[0.0, 1.393249]),
        Solution(f_opt=-0.6736675, x_opt=[1.393249, 0.0]),
    ],
    _ref=["jamil2013"],
)
def keane(xy: Sequence[float]) -> float:
    """Keane Function."""
    x, y = xy[0], xy[1]
    n = (sin(x - y) ** 2) * (sin(x + y) ** 2)
    d = sqrt(x**2 + y**2)
    return -safe_div(n, d)


@benchmark(
    bounds=[
        (-1.2, 1.2),
        (-1.2, 1.2),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0, 1.0])],
    _ref=["lavi1966"],
)
def leon(xy: Sequence[float]) -> float:
    """Leon Function."""
    x, y = xy[0], xy[1]
    return 100 * (y - x**2) ** 2 + (1 - x) ** 2


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0, 1.0])],
    _ref=["wikipedia_test_functions"],
)
def levi_n13(xy: Sequence[float]) -> float:
    """Lévi Function N.13."""
    x, y = xy[0], xy[1]
    return (
        sin(3.0 * pi * x) ** 2
        + (x - 1) ** 2 * (1 + sin(3.0 * pi * y) ** 2)
        + (y - 1) ** 2 * (1 + sin(2.0 * pi * y) ** 2)
    )


@benchmark(
    bounds=[
        (-10.0, 10.0),
        (-10.0, 10.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["wikipedia_test_functions"],
)
def matyas(xy: Sequence[float]) -> float:
    """Matyas Function."""
    x, y = xy[0], xy[1]
    return 0.26 * (x**2 + y**2) - 0.48 * x * y


@benchmark(
    bounds=[(0.0, pi)],
    dimensions=None,
    g_opt=[Solution(f_opt=-1.8013, x_opt=[2.2, 1.57])],
    _ref=["surjanovic_michalewicz"],
)
def michalewicz(x: Sequence[float], m: float = 10) -> float:
    """Michalewicz Function.

    The parameter m defines the steepness of valleys and ridges (default m = 10).
    A larger m leads to a more difficult search.
    """
    d = len(x)
    result = 0
    for i in range(d):
        result -= sin(x[i]) * (sin((i + 1) * x[i] ** 2 / pi)) ** (2 * m)
    return result


@benchmark(
    bounds=[
        (-1.5, 4.0),
        (-3.0, 4.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=-1.91322295, x_opt=[-0.54719, -1.54719])],
    _ref=["wikipedia_test_functions"],
)
def mccormick(xy: Sequence[float]) -> float:
    """McCormick Function."""
    x, y = xy[0], xy[1]
    return sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1


@benchmark(
    bounds=[
        (-5.0, 5.0),
        (-5.0, 5.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=0.0, x_opt=[-3 * pi / 2, -pi]),
        Solution(f_opt=0.0, x_opt=[-3 * pi / 2, 0.0]),
        Solution(f_opt=0.0, x_opt=[-3 * pi / 2, pi]),
        Solution(f_opt=0.0, x_opt=[-pi / 2, -pi]),
        Solution(f_opt=0.0, x_opt=[-pi / 2, 0.0]),
        Solution(f_opt=0.0, x_opt=[-pi / 2, pi]),
        Solution(f_opt=0.0, x_opt=[pi / 2, -pi]),
        Solution(f_opt=0.0, x_opt=[pi / 2, 0.0]),
        Solution(f_opt=0.0, x_opt=[pi / 2, pi]),
        Solution(f_opt=0.0, x_opt=[3 * pi / 2, -pi]),
        Solution(f_opt=0.0, x_opt=[3 * pi / 2, 0.0]),
        Solution(f_opt=0.0, x_opt=[3 * pi / 2, pi]),
    ],
    _ref=["parsopoulos2001"],
)
def parsopoulos(xy: Sequence[float]) -> float:
    """Parsopoulos Function.

    Features an infinite number of periodic global minima in R^2 at
    x* = (k*pi/2, l*pi) for odd k and integer l.
    """
    return cos(xy[0]) ** 2 + sin(xy[1]) ** 2


@benchmark(
    bounds=[
        (-11.0, 11.0),
        (-11.0, 11.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=-0.9635348, x_opt=[9.6461677, 9.6461676]),
        Solution(f_opt=-0.9635348, x_opt=[-9.6461677, 9.6461676]),
        Solution(f_opt=-0.9635348, x_opt=[9.6461677, -9.6461676]),
        Solution(f_opt=-0.9635348, x_opt=[-9.6461677, -9.6461676]),
    ],
    _ref=["mishra2006"],
)
def pen_holder(xy: Sequence[float]) -> float:
    """Pen Holder Function."""
    return -exp(
        -(
            (
                abs(
                    cos(xy[0])
                    * cos(xy[1])
                    * exp(abs(1 - sqrt(xy[0] ** 2 + xy[1] ** 2) / pi))
                )
            )
            ** -1
        )
    )


@benchmark(
    bounds=[(-5.12, 5.12)],
    dimensions=None,
    g_opt=[Solution(f_opt=30.0, x_opt=[0.0])],
    _ref=["wikipedia_test_functions"],
)
def plateau(x: Sequence[float]) -> float:
    """Plateau Function."""
    return 30 + sum([floor(abs(v)) for v in x])


@benchmark(
    bounds=[(-500.0, 500.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0])],
    _ref=["qing2006"],
)
def qing(x: Sequence[float]) -> float:
    """Qing Function."""
    return sum([(v**2 - (i + 1)) ** 2 for i, v in enumerate(x)])


@benchmark(
    bounds=[(-1.28, 1.28)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["storn1995"],
)
def quartic(x: Sequence[float]) -> float:
    """Quartic Function (without noise term)."""
    return sum([(i + 1) * v**4 for i, v in enumerate(x)])


@benchmark(
    bounds=[(-5.12, 5.12)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["wikipedia_rastrigin"],
)
def rastrigin(x: Sequence[float], safe_mode: bool = False) -> float:
    """Rastrigin Function."""
    if safe_mode:
        for item in x:
            assert item <= 5.12 and item >= -5.12, (
                "input exceeds bounds of [-5.12, 5.12]"
            )
    return len(x) * 10.0 + sum(
        [item * item - 10.0 * cos(2.0 * pi * item) for item in x]
    )


@benchmark(
    bounds=[(-65.536, 65.536)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["molga2005"],
)
def rotated_hyper_ellipsoid(xy: Sequence[float]) -> float:
    """Rotated Hyper-Ellipsoid Function."""
    a = 0.0
    for i in range(len(xy)):
        a += sum([xy[j] ** 2 for j in range(i + 1)])
    return a


@benchmark(
    bounds=[(-5.0, 10.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0])],
    _ref=["wikipedia_rosenbrock"],
)
def rosenbrock(x: Sequence[float]) -> float:
    """Rosenbrock Function (Rosenbrock's Valley / Banana Function)."""
    total = 0.0
    for i in range(len(x) - 1):
        total += 100 * (x[i + 1] - x[i] * x[i]) ** 2 + (1 - x[i]) ** 2
    return total


@benchmark(
    bounds=[(-100.0, 100.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["salomon1996"],
)
def salomon(x: Sequence[float]) -> float:
    """Salomon Function."""
    return (
        1
        - cos(2 * pi * sqrt(sum([v**2 for v in x])))
        + 0.1 * sqrt(sum([v**2 for v in x]))
    )


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0])],
    _ref=["surjanovic_schaffer_n2"],
)
def schaffer_n2(xy: Sequence[float]) -> float:
    """Schaffer Function N.2."""
    x, y = xy[0], xy[1]
    return 0.5 + (sin(x**2 - y**2) ** 2 - 0.5) / (1 + 0.001 * (x**2 + y**2)) ** 2


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[
        Solution(f_opt=0.292579, x_opt=[0.0, 1.25313]),
        Solution(f_opt=0.292579, x_opt=[0.0, -1.25313]),
        Solution(f_opt=0.292579, x_opt=[1.25313, 0.0]),
        Solution(f_opt=0.292579, x_opt=[-1.25313, 0.0]),
    ],
    _ref=["surjanovic_schaffer_n4"],
)
def schaffer_n4(xy: Sequence[float]) -> float:
    """Schaffer Function N.4."""
    x, y = xy[0], xy[1]
    return (
        0.5 + (cos(sin(abs(x**2 - y**2))) ** 2 - 0.5) / (1 + 0.001 * (x**2 + y**2)) ** 2
    )


@benchmark(
    bounds=[(-500.0, 500.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[420.968746359982025])],
    _ref=["surjanovic_schwefel"],
)
def schwefel(x: Sequence[float]) -> float:
    """Schwefel Function."""
    return 418.9828872724337 * len(x) - sum([item * sin(sqrt(abs(item))) for item in x])


@benchmark(
    bounds=[(-5.12, 5.12)],
    _ref=["wikipedia_test_functions"],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
)
def sphere(x: Sequence[float]) -> float:
    """Sphere Function."""
    return sum([item * item for item in x])


@benchmark(
    bounds=[(-100.0, 100.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["jamil2013"],
)
def step(xy: Sequence[float]) -> float:
    """Step Function."""
    return sum([floor(abs(v)) for v in xy])


@benchmark(
    bounds=[(-5.0, 5.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=-39.1661657, x_opt=[-2.903534])],
    _ref=["wikipedia_test_functions"],
)
def styblinski_tang(x: Sequence[float]) -> float:
    """Styblinski-Tang Function."""
    return sum([item**4 - 16 * item**2 + 5 * item for item in x]) / 2.0


@benchmark(
    bounds=[(-1.0, 1.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["surjanovic_sum_powers"],
)
def sum_of_different_powers(x: Sequence[float]) -> float:
    """Sum of Different Powers Function."""
    return sum([abs(item) ** (i + 2) for i, item in enumerate(x)])


@benchmark(
    bounds=[(-10.0, 10.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["hedar2005"],
)
def sum_of_squares(xy: Sequence[float]) -> float:
    """Sum of Squares Function."""
    return sum([(i + 1) * v**2 for i, v in enumerate(xy)])


@benchmark(
    bounds=[(-100.0, 100.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[1.0])],
    _ref=["hedar2005"],
)
def trid(xy: Sequence[float]) -> float:
    """Trid Function."""
    a = sum([(v - 1) ** 2 for v in xy])
    b = sum([(xy[i + 1] * xy[i]) for i, v in enumerate(xy[1:])])
    return a - b


@benchmark(
    bounds=[
        (-100.0, 100.0),
        (-100.0, 100.0),
    ],
    dimensions=2,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, -50.0])],
    _ref=["rahnamayan2007_novel"],
)
def tripod(xy: Sequence[float]) -> float:
    """Tripod Function."""
    x1, x2 = xy[0], xy[1]
    p_x1 = 1 if x1 >= 0 else 0
    p_x2 = 1 if x2 >= 0 else 0

    a = p_x2 * (1 + p_x1)
    b = abs(x1 + 50 * p_x2 * (1 - 2 * p_x1))
    c = abs(x2 + 50 * (1 - 2 * p_x2))
    return a + b + c


@benchmark(
    bounds=[
        (0.0, 2.0),
        (0.0, 2.0),
        (0.0, 2.0),
    ],
    dimensions=3,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0, 0.0, 0.0])],
    _ref=["schwefel1981"],
)
def wolfe(xyz: Sequence[float]) -> float:
    """Wolfe Function."""
    x, y, z = xyz[0], xyz[1], xyz[2]
    return float((4.0 / 3.0) * (x**2 + y**2 - x * y) ** 0.75 + z)


@benchmark(
    bounds=[(-5.0, 10.0)],
    dimensions=None,
    g_opt=[Solution(f_opt=0.0, x_opt=[0.0])],
    _ref=["rahnamayan2007_novel"],
)
def zakharov(x: Sequence[float]) -> float:
    """Zakharov Function."""
    a, b = 0.0, 0.0
    for i, val in enumerate(x):
        a += val**2
        b += 0.5 * (i + 1) * val
    return a + b**2 + b**4


class tsp:
    """Travelling Salesman Problem (TSP).

    References
    ----------
      [1] Wikipedia. (2020). Travelling salesman problem. https://en.wikipedia.org/wiki/Travelling_salesman_problem
    """

    def __init__(
        self, dist_func: Callable[[Any, Any], float], close_loop: bool = True
    ) -> None:
        self.dist_func = dist_func
        self.close_loop = close_loop

    def dist(self, xy: Sequence[Any]) -> float:
        # sequentially calculate distance between all tsp nodes
        dist = 0.0
        for i in range(len(xy) - 1):
            dist += self.dist_func(xy[i + 1], xy[i])

        # close the tsp loop by calculating the distance
        # between the first and last points
        if self.close_loop:
            dist += self.dist_func(xy[0], xy[-1])

        return dist


# --- END ----------------------------------------------------------------------+
