#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy and contributors
#   Nov. 2019
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from math import cos
from math import e
from math import exp
from math import floor
from math import pi
from math import sin
from math import sqrt

#--- FUNCTIONS ----------------------------------------------------------------+


def ackley(xy):
    '''
    Ackley Function

    wikipedia: https://en.wikipedia.org/wiki/Ackley_function

    global minium at f(x=0, y=0) = 0
    bounds: -5<=x,y<=5
    '''
    x, y = xy[0], xy[1]
    return (-20 * exp(-0.2 * sqrt(0.5 * (x*x + y*y))) -
            exp(0.5 * (cos(2.0*pi*x) + cos(2*pi*y))) + e + 20)


def ackley_n2(xy):
    '''Ackley N.2

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=-200 at x=(0,0)
    bounds: x_i in [-32, 32] for i=1,2

    References
    ----------
    D. H. Ackley, “A Connectionist Machine for Genetic Hill-Climbing,” Kluwer,
    1987.
    '''
    x, y = xy[0], xy[1]
    return -200*exp(-0.2 * sqrt(x**2 + y**2))


def adjiman(xy):
    '''Adjiman Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    bounds: x in [-1,2], y in [-1,1]
    global minimum: f(x)=-2.02180678 at x=[2.0, 0.10578]

    References
    ----------
    C. S. Adjiman, S. Sallwig, C. A. Flouda, A. Neumaier, “A Global Optimization
    Method, aBB for General Twice-Differentiable NLPs-1, Theoretical Advances,”
    Computers Chemical Engineering, vol. 22, no. 9, pp. 1137-1158, 1998.
    '''

    x, y = xy[0], xy[1]
    return (cos(x) * sin(y)) - (x / (y**2.0 + 1.0))


def bartels_conn(xy):
    '''Bartels Conn Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: x_i in [-500, 500] for i=1,2
    Global minimum: f(x)=1 at x=[0,0]

    References
    ----------
    Momin Jamil and Xin-She Yang, A literature survey of benchmark functions for
    global optimization problems, Int. Journal of Mathematical Modelling and
    Numerical Optimisation, Vol. 4, Issue. 2 (2013).
    '''
    x1, x2 = xy[0], xy[1]
    return abs(x1**2 + x2**2 + x1*x2) + abs(sin(x1)) + abs(cos(x2))


def beale(xy):
    '''
    Beale Function

    global minimum: f(x=3, y=0.5) = 0
    bounds: -4.5 <= x, y <= 4.5
    '''
    x, y = xy[0], xy[1]
    return ((1.500 - x + x*y)**2 +
            (2.250 - x + x*y**2)**2 +
            (2.625 - x + x*y**3)**2)


def bird(xy):
    '''Bird Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum(s): f(x) = -106.76453 at
        x=[ 4.70105,  3.15294] and
        x=[-1.58214, -3.13024]

    bounds: x_i in [-2*pi, 2*pi] for i=1,2

    References
    ----------
    S. K. Mishra, “Global Optimization By Differential Evolution and Particle
    Swarm Methods: Evaluation On Some Benchmark Functions,” Munich Research
    Papers in Economics, [Available Online]:
    http://mpra.ub.uni-muenchen.de/1005/
    '''
    x, y = xy[0], xy[1]
    return sin(x)*exp((1-cos(y))**2) + cos(y)*exp((1-sin(x))**2) + (x-y)**2


def bohachevsky_n1(xy):
    '''Bohachevsky N.1

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimim: f(x*)=0 at x*=(0,0)
    bounds: x_i in [-100, 100] for i=1,2

    References
    ----------
    [1] I. O. Bohachevsky, M. E. Johnson, M. L. Stein, “General Simulated Annealing
    for Function Optimization,” Technometrics, vol. 28, no. 3, pp. 209-217,
    1986.

    [2] http://www.sfu.ca/~ssurjano/boha.html
    '''

    x, y = xy[0], xy[1]
    return x**2 + 2*y**2 - 0.3*cos(3.0*pi*x) - 0.4*cos(4*pi*y) + 0.7


def bohachevsky_n2(xy):
    '''Bohachevsky N.2

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimim: f(x*)=0 at x*=(0,0)
    bounds: x_i in [-100, 100] for i=1,2

    References
    ----------
    [1] I. O. Bohachevsky, M. E. Johnson, M. L. Stein, “General Simulated Annealing
    for Function Optimization,” Technometrics, vol. 28, no. 3, pp. 209-217,
    1986.

    [2] http://www.sfu.ca/~ssurjano/boha.html
    '''

    x, y = xy[0], xy[1]
    return x**2 + 2*y**2 - 0.3*cos(3*pi*x)*cos(4*pi*y) + 0.3


def bohachevsky_n3(xy):
    '''Bohachevsky N.3

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimim: f(x*)=0 at x*=(0,0)
    bounds: x_i in [-100, 100] for i=1,2

    References
    ----------
    [1] I. O. Bohachevsky, M. E. Johnson, M. L. Stein, “General Simulated Annealing
    for Function Optimization,” Technometrics, vol. 28, no. 3, pp. 209-217,
    1986.

    [2] http://www.sfu.ca/~ssurjano/boha.html
    '''
    x, y = xy[0], xy[1]
    return x**2 + 2*y**2 - 0.3*cos(3*pi*x + 4*pi*y) + 0.3


def booth(xy):
    '''
    Booth Function

    global minimum: f(x=1, y=3) = 0
    bounds: 10 <= x, y <= 10
    '''
    x, y = xy[0], xy[1]
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2


def branin(xy):
    '''
    Branin Function

    Reference: https://www.sfu.ca/~ssurjano/branin.html

    global minimum(s):
        f(x=-pi, y=12.275) = 0.397887
        f(x= pi, y= 2.275) = 0.397887
        f(x=9.42478, y=2.475) = 0.397887
    bounds:
        -5 <= x <= 10
        0 <= y <= 15
    '''
    a = 1
    b = 5.1 / (4 * pi**2)
    c = 5 / pi
    r = 6
    s = 10
    t = 1/(8*pi)
    x, y = xy[0], xy[1]
    return a * (y - b*x**2 + c*x - r)**2 + s*(1-t)*cos(x) + s


def brent(xy):
    '''Brent Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x)=0 at x=[-10, -10]]
    bounds: x_i=[-10, 2] for i=1,2

    References
    ----------
    S. K. Mishra, “Global Optimization By Differential Evolution and Particle
    Swarm Methods: Evaluation On Some Benchmark Functions,” Munich Research
    Papers in Economics, [Available Online]:
    http://mpra.ub.uni-muenchen.de/1005/
    '''

    x, y, = xy[0], xy[1]
    return (x + 10.0)**2.0 + (y + 10.0)**2.0 + exp(-x**2.0 - y**2.0)


def brown(x):
    '''Brown Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x)=0 at x=(0,...,0)
    bounds: x_i in [-1,4] for i=1,...,n

    References
    ----------
    O. Begambre, J. E. Laier, “A hybrid Particle Swarm Optimization - Simplex
    Algorithm (PSOS) for Structural Damage Identification,” Journal of Advances
    in Engineering Software, vol. 40, no. 9, pp. 883-891, 2009.
    '''

    return sum([
        ((x[i]**2)**(x[i+1]**2 + 1.0)) +
        ((x[i+1]**2)**(x[i]+1.0))
        for i in range(len(x)-1)])


def bukin_n6(xy):
    '''
    Bukin Function N.6

    global minimum: f(x=-10, y=1) = 0
    bounds:
        -15 <= x <= -5
        -3 <= y <= 3
    '''
    x, y = xy[0], xy[1]
    return 100 * sqrt(abs(y-0.01*x**2)) + 0.01*abs(x+10)


def camel_hump_3(xy):
    '''
    Three-Hump Camel Function

    global minimum: f(x=0, y=0) = 0
    bounds: -5 <= x, y <= 5
    '''
    x, y = xy[0], xy[1]
    return 2.0*x**2 - 1.05*x**4 + (x**6 / 6.0) + x*y + y**2


def camel_hump_6(xy):
    '''Six-Hump Camel Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    The six-hump camel function is usually evaluated on the rectangle bounded
    by:
        x in [-3, 3]
        y in [-2, 2]

    Global minimum(s):
        1) f( 0.0898, -0.7126) = -1.0316
        2) f(-0.0898,  0.7126) = -1.0316

    References
    ----------
    Molga, M., & Smutnicki, C. Test functions for optimization needs (2005)
    '''

    x, y = xy[0], xy[1]
    a = (4-(2.1*x**2)+(x**4)/3.0) * x**2
    b = x*y
    c = (-4+(4*y**2)) * y**2
    return a + b + c


def colville(xy):
    '''Colville Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: The Colville function is a 4-dimensional function usually evaluated
    on the hypercube defined by x_i in [-10, 10] for i=1,2,3,4.

    Global minimum: f(x)=0 at x=[1,1,1,1]

    References
    ----------
    A.-R. Hedar, “Global Optimization Test Problems”
    '''

    x1, x2, x3, x4 = xy[0], xy[1], xy[2], xy[3]
    a = 100*(x1**2 - x2)**2
    b = (x1-1)**2
    c = (x3-1)**2
    d = 90*(x3**2 - x4)**2
    e = 10.1*((x2-1)**2 + (x4-1)**2)
    f = 19.8*(x2-1)*(x4-1)
    return a + b + c + d + e + f


def cross_in_tray(xy):
    '''
    Cross-in-tray Fucntion

    global minimum:
        f(x=1.34941, y=1.34941) = -2.06261
        f(x=1.34941, y=-1.34941) = -2.06261
        f(x=-1.34941, y=1.34941) = -2.06261
        f(x=-1.34941, y=-1.34941) = -2.06261
    bounds: -10 = x, y <= 10
    '''
    x, y = xy[0], xy[1]
    return -0.0001*(abs(sin(x)*sin(y)*exp(abs(100-(sqrt(x**2 + y**2)/pi))))+1)**0.1


def deckkers_aarts(xy):
    '''Deckkers-Aarts Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=-24771.093749 at x*=[0, 15] and x*=[0, -15]
    bounds: x_i in [-20, 20] for i=1,2

    References
    ----------
    M. M. Ali, C. Khompatraporn, Z. B. Zabinsky, “A Numerical Evaluation of
    Several Stochastic Algorithms on Selected Continuous Global Optimization
    Test Problems,” Journal of Global Optimization, vol. 31, pp. 635-672, 2005.
    '''

    x, y = xy[0], xy[1]
    return 10*5 * x**2 + y**2 - (x**2 + y**2)**2 + 10**(-5) * (x**2 + y**2)**4


def dixon_price(x):
    '''Dixon and Price Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=0 at x_i = 2^-(((2^i)-2)/(2^i))
    bounds: x_i in [-10, 10] for i=1,...,n

    References
    ----------
    L. C. W. Dixon, R. C. Price, “The Truncated Newton Method for Sparse
    Unconstrained Optimisation Using Automatic Differentiation,” Journal of
    Optimization Theory and Applications, vol. 60, no. 2, pp. 261-275, 1989.
    '''
    return (x[0] - 1.0)**2.0 + sum([i*(2.0*x[i]**2.0 - x[i-1])**2.0 for i in range(1, len(x))])


def drop_wave(xy):
    '''
    Drop-Wave Function

    link: https://www.sfu.ca/~ssurjano/drop.html

    global minimum: f(x=0, y=0) = -1
    bounds: -5.12 <= x, y <= 5.12
    '''
    x, y = xy[0], xy[1]
    return -(1 + cos(12 * sqrt(x**2 + y**2))) / (0.5 * (x**2 + y**2) + 2)


def easom(xy):
    '''
    Easom Function

    global minimum: f(x=pi, y=pi) = -1
    bounds: -100 <= x, y <= 100
    '''
    x, y = xy[0], xy[1]
    return -cos(x)*cos(y)*exp(-((x-pi)**2 + (y-pi)**2))


def eggholder(xy):
    '''
    Eggholder Function

    global minimum: f(x=512, y=404.2319) = -959.6407
    bounds: -512 <= x, y <= 512
    '''
    x, y = xy[0], xy[1]
    return (-(y+47)*sin(sqrt(abs((x/2.0) + (y+47)))) -
            x*sin(sqrt(abs(x-(y+47)))))


def exponential(x):
    '''Exponential Function

    Parameters
    ----------
        x: list or 1-d numpy array

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=-1 at x*=(0,..,0)
    bounds: x_i in [-1, 1] for i=1,2

    References
    ----------
    S. Rahnamyan, H. R. Tizhoosh, N. M. M. Salama, “Opposition-Based
    Differential Evolution (ODE) with Variable Jumping Rate,” IEEE Sympousim
    Foundations Computation Intelligence, Honolulu, HI, pp. 81-88, 2007.
    '''
    return -exp(-0.5*sum([v**2 for v in x]))


def goldstein_price(xy):
    '''
    Goldstein-Price Function

    global minimum: f(0, -1) = 3
    bounds: -2 <= x, y <= 2
    '''
    x, y = xy[0], xy[1]
    return ((1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) *
            (30 + (2*x-3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)))


def griewank(xy):
    '''Griwank Function

    Parameters
    ----------
        x: list or 1-d numpy array

    Returns
    -------
        float

    Notes
    -----
    Bounds: x_i in [-600, 600] for all i=1,...,d
    Global minimum: f(x)=0 at x=(0,...,0)

    References
    ----------
    A. O. Griewank, “Generalized Descent for Global Optimization,” Journal of
    Optimization Theory and Applications, vol. 34, no. 1, pp. 11-39, 1981.
    '''

    a, b, = 0, 1
    for i, v in enumerate(xy):
        a += v**2 / 4000.0
        b *= cos(v/sqrt(i+1))
    return a - b + 1


def himmelblau(xy):
    '''
    Himmelblau's Function

    wikipedia: https://en.wikipedia.org/wiki/Himmelblau%27s_function

    global minimum(s):
        f(x=3.0, 2.0) = 0
        f(-2.805118, 3.131312) = 0
        f(-3.779310, -3.283186) = 0
        f(3.584428, -1.848126) = 0
    bounds: -5 <= x, y <= 5
    '''
    x, y = xy[0], xy[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def holder_table(xy):
    '''
    Holder Table Function

    global minimum:
        f(x= 8.05502, y= 9.66459) = -19.2085
        f(x=-8.05502, y= 9.66459) = -19.2085
        f(x= 8.05502, y=-9.66459) = -19.2085
        f(x=-8.05502, y=-9.66459) = -19.2085
    bounds: -10 <= x, y <= 10
    '''
    x, y = xy[0], xy[1]
    return -abs(sin(x)*cos(y)*exp(abs(1-(sqrt(x**2 + y**2)/pi))))


def hosaki(xy):
    '''Hosaki Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=-2.345811 at x*=[4,2]
    bounds:
        x1 in [0, 5]
        x2 in [0, 6]

    References
    ----------
    G. A. Bekey, M. T. Ung, “A Comparative Evaluation of Two Global Search
    Algorithms,” IEEE Transaction on Systems, Man and Cybernetics, vol. 4,
    no. 1, pp. 112-116, 1974.
    '''
    x, y = xy[0], xy[1]
    return (1 - 8*x + 7*x**2 - (7.0/3.0)*x**3 + 0.25*x**4) * y**2 * exp(-y)


def keane(xy):
    '''Keane Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=0.6736675 at:
        x* = [0, 1.3932490]
        x* = [1.3932490, 0]
    bounds: x_i in [-10, 10] for i=1,2

    References
    ----------
    Momin Jamil and Xin-She Yang, A literature survey of benchmark functions for
    global optimization problems, Int. Journal of Mathematical Modelling and
    Numerical Optimisation}, Vol. 4, No. 2, pp. 150–194 (2013), arXiv:1308.4008
    '''
    x, y = xy[0], xy[1]
    n = (sin(x-y)**2) * (sin(x+y)**2)
    d = sqrt(x**2 + y**2)
    return n / d


def leon(xy):
    '''Leon Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=0 at x*=(1,1)
    bounds: x_i in [-10, 10] for i=1,2

    References
    ----------
     A. Lavi, T. P. Vogel (eds), “Recent Advances in Optimization Techniques,”
     John Wliley & Sons, 1966.
    '''
    x, y = xy[0], xy[1]
    return 100*(y-x**3)*2 + (1-x)**2


def levi_n13(xy):
    '''
    Levi Function N.13

    global minimum: f(x=1, y=1) = 0
    bounds: -10 <= x, y <= 10
    '''
    x, y = xy[0], xy[1]
    return sin(3.0*pi*x)**2 + (x-1)**2 * (1+sin(3.0*pi*y)**2) + (y-1)**2 * (1+sin(2.0*pi*y)**2)


def matyas(xy):
    '''
    Matyas Function

    global minimum: f(x=0, y=0) = 0
    bounds: -10 <= x, y <= 10
    '''
    x, y = xy[0], xy[1]
    return 0.26*(x**2 + y**2) - 0.48*x*y


def michalewicz(x, m=10):
    '''Michalewicz Function

    Parameters
    ----------
        x : list
        m : float
    Returns
    -------
        float

    Notes
    -----
    The parameter m defines the steepness of they valleys and ridges; a larger m leads to a more difficult search. The recommended value of m is m = 10.
    global minimum for 2D: f(x)=-1.8013 at x*=(2.20,1.57)
    bounds: x_i in [0, π] for i=1,..., d
    '''
    d = len(x)
    result = 0
    for i in range(d):
        result -= sin(x[i])*(sin((i+1)*x[i]**2/pi))**(2*m)
    return result


def mccormick(xy):
    '''
    McCormick Function

    global minimum: f(x=-0.54719, y=-1.54719) = -1.9133
    bounds:
        -1.5 <= x <= 4
        -3 <= y <= 4
    '''
    x, y = xy[0], xy[1]
    return sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1


def parsopoulos(xy):
    '''Parsopoulos Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    there are infinate global minimums in R^2
    global minimum(s):
        f(x*)=0 at x*=(k*pi/2, l*pi)
        where:
            k=(+/-)1, (+/-)3,...
            l = 0, (+/-)1, (+/-)2,...
    bounds: x_i in [-11,11] for i=1,2

    References
    ----------

    '''
    return cos(xy[0])**2 + sin(xy[1])**2


def pen_holder(xy):
    '''Pen Holder Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    global minimum(s):
        f(x*)=-0.9635348 at x*=[ 9.6461677,  9.6461676]
        f(x*)=-0.9635348 at x*=[-9.6461677,  9.6461676]
        f(x*)=-0.9635348 at x*=[ 9.6461677, -9.6461676]
        f(x*)=-0.9635348 at x*=[-9.6461677, -9.6461676]

    bounds: x_i in [-11, 11] for i=1,2

    References
    ----------
    S. K. Mishra, “Global Optimization By Differential Evolution and Particle
    Swarm Methods: Evaluation On Some Benchmark Functions,” Munich Research
    Papers in Economics, [Available Online]:
    http://mpra.ub.uni-muenchen.de/1005/
    '''

    return -exp(-(abs(cos(xy[0])*cos(xy[1])*exp(abs(1 - sqrt(xy[0]**2 + xy[1]**2)/pi))))**-1)


def plateau(x):
    '''Plateau Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=30 at x*=(0,...,0)
    bounds: x_i in [-5.12, 5.12] for i=1,...,n
    '''

    return 30 + sum([floor(abs(v)) for v in x])


def qing(x):
    '''Qing Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=0 at x*=(+/-sqrt(i),...,+/-sqrt(i))
    bounds: x_i in [-500, 500] for i=1,...,n

    References
    ----------
    A. Qing, “Dynamic Differential Evolution Strategy and Applications in
    Electromagnetic Inverse Scattering Problems,” IEEE Transactions on
    Geoscience and remote Sensing, vol. 44, no. 1, pp. 116-125, 2006.
    '''
    return sum([(v**2 - (i+1))**2 for i, v in enumerate(x)])


def rastrigin(x, safe_mode=False):
    '''Rastrigin Function

    Parameters
    ----------
        x : list
        safe_mode : bool (optional, default = False)

    Returns
    -------
        float

    Notes
    -----
    Bounds: -5.12 <= x_i <= 5.12 for all i=1,...,d
    Global minimum: f(x)=0 at x=(0,...,0)

    References
    ----------
    wikipedia: https://en.wikipedia.org/wiki/Rastrigin_function
    '''

    if safe_mode:
        for item in x:
            assert x<=5.12 and x>=-5.12, 'input exceeds bounds of [-5.12, 5.12]'
    return len(x)*10.0 +  sum([item*item - 10.0*cos(2.0*pi*item) for item in x])


def rotated_hyper_ellipsoid(xy):
    '''Rotated Hyper-Ellipsoid

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: the rotated hyper-ellipsoid is usually evaluated on the hypercube
    defined by x_i in [-65.536, 65.536] for all i=1,...,d

    Global minimum: f(x)=0 at x=(0,...,0)

    References
    ----------
    Molga, M., & Smutnicki, C. Test functions for optimization needs (2005)
    '''
    a = 0
    for i in range(0, len(xy)): a += sum([xy[j]**2 for j in range(0, i)])
    return a


def rosenbrock(x):
    '''
    Rosenbrock Function

    wikipedia: https://en.wikipedia.org/wiki/Rosenbrock_function

    global minimum:
        n=2 -> f(1,1)=0
        n=3 -> f(1,1,1)=0
        n>3 -> f(1,...,1)=0
    bounds:
        -inf <= x_i <= +inf
        1 <= i <= n
    '''

    total = 0
    for i in range(len(x)-1):
        total += 100*(x[i+1] - x[i]*x[i])**2 + (1-x[i])**2
    return total


def salomon(x):
    '''Salomon Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x*)=0 at x*=(0,...,0)
    bounds: x_i in [-100, 100] for i=1,...,n

    Reference
    ---------
    R. Salomon, “Re-evaluating Genetic Algorithm Performance Under Corodinate
    Rotation of Benchmark Functions: A Survey of Some Theoretical and Practical
    Aspects of Genetic Algorithms,” BioSystems, vol. 39, no. 3, pp. 263-278,
    1996.
    '''
    return 1 - cos(2*pi*sqrt(sum([v**2 for v in x]))) + 0.1*sqrt(sum([v**2 for v in x]))


def schaffer_n2(xy):
    '''
    Schaffer Function N.2

    Reference: https://www.sfu.ca/~ssurjano/schaffer2.html

    global minimum: f(x=0, y=0) = 0
    bounds: -100 <= x, y <= 100
    '''
    x, y = xy[0], xy[1]
    return 0.5 + (sin(x**2 - y**2)**2 - 0.5)/(1+0.001*(x**2+y**2))**2


def schaffer_n4(xy):
    '''
    Schaffer Function N.4

    Reference: https://www.sfu.ca/~ssurjano/schaffer4.html

    global minimum:
        f(x=0, y= 1.25313) = 0.292579
        f(x=0, y=-1.25313) = 0.292579
    bounds: -100 <= x, y <= 100
    '''
    x, y = xy[0], xy[1]
    return 0.5 + (cos(sin(abs(x**2 - y**2)))**2 - 0.5)/(1+0.001*(x**2 + y**2))**2


def schwefel(x):
    '''
    Schwefel Function

    reference: https://www.sfu.ca/~ssurjano/schwef.html

    global minimum: f(x) = 0 when x = [420.9687,...,420.9687]
    bounds: -500 <= x_i <= 500
    '''
    return 418.9829*len(x) - sum([item * sin(sqrt(abs(item))) for item in x])


def sphere(x):
    '''
    Sphere Function

    global minimum at x=0 where f(x)=0
    bounds: none
    '''
    return sum([item * item for item in x])


def step(xy):
    '''Step Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: x_i in [-100, 100] for i=1,...,d
    Global minimum: f(x)=0 at x=[0,...,0]

    References
    ----------
    Momin Jamil and Xin-She Yang, A literature survey of benchmark functions for
    global optimization problems, Int. Journal of Mathematical Modelling and
    Numerical Optimisation, Vol. 4, Issue. 2 (2013).
    '''
    return sum([floor(abs(v)) for v in xy])


def styblinski_tang(x):
    '''
    Styblinski-Tang Function

    global minimum:
        -39.16617n < f(-2.903534,...,-2.903534) < -39.16616n
    bounds:
        -5 <= x_i <= 5
        1 <= i <= n
    '''
    return sum([item**4 - 16*item**2 + 5*item for item in x]) / 2.0


def sum_of_different_powers(x):
    '''
    Sum of Different Powers
    reference: https://www.sfu.ca/~ssurjano/sumpow.html
    global minimum: f(x)=0, when x=[0,...,0]
    '''
    return sum([abs(item)**(i+2) for i, item in enumerate(x)])


def sum_of_squares(xy):
    '''Sum of Squares Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: x_i in [-10, 10] for all i=1,...,d
    Global minimum: f(x)=0 at x=(0,...,0)

    References
    ----------
    A.-R. Hedar, “Global Optimization Test Problems”
    '''
    return sum([(i+1) * v**2 for i, v in enumerate(xy)])


def trid(xy):
    '''Trid Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: x in [-d^2, d^2] for i=1,...,d
    Global minimum: f(x)=-d(d+4)(d-1)/6 at x_i=i(d+1-i) for all i=1,...,d

    References
    ----------
    A.-R. Hedar, “Global Optimization Test Problems”
    '''
    a = sum([(v-1)**2 for v in xy])
    b = sum([(xy[i+1]*xy[i]) for i, v in enumerate(xy[1:])])
    return a - b


def tripod(xy):
    '''Tripod Function

    Parameters
    ----------
        xy : list

    Returns
    -------
        float

    Notes
    -----
    Bounds: x_i in [-100, 100] for i=1,2
    Global minimum: f(x)=0 at x=[0,-50]

    References
    ----------
    S. Rahnamyan, H. R. Tizhoosh, N. M. M. Salama, “A Novel Population
    Initialization Method for Accelerating Evolutionary Algorithms”
    Computers and Mathematics with Applications, vol. 53, no. 10,
    pp. 1605-1614, 2007.
    '''

    x1, x2 = xy[0], xy[1]
    p_x1 = 1 if x1>=0 else 0
    p_x2 = 1 if x2>=0 else 0

    a = p_x2 * (1 + p_x1)
    b = abs(x1 + 50*p_x2*(1-2*p_x1))
    c = abs(x2 + 50*(1-2*p_x2))
    return a + b + c


def wolfe(xyz):
    '''Wolfe Function

    Parameters
    ----------
        xyz : list

    Returns
    -------
        float

    Notes
    -----
    global minimum: f(x)=0 at x=[0,0,0]
    bounds: x_i in [0, 2] for i=1,2,3

    References
    ----------
    H. P. Schwefel, “Numerical Optimization for Computer Models,” John Wiley
    Sons, 1981.
    '''
    x, y, z = xyz[0], xyz[1], xyz[2]
    return (4.0/3.0)*(x**2.0 + y**2.0 - x*y)**0.75 + z


def zakharov(x):
    '''Zakharov Function

    Parameters
    ----------
        x : list

    Returns
    -------
        float

    Notes
    -----
    The Zakharov has no local minima except a single global one.

    Bounds:
        The function is usually evaluated within the hypercube defined by
        x_i in [-5, 10] for i = 1,...,d

    Global minimum:
        f(x) = 0 at x = (0,...,0)

    References
    ----------
    Shahryar Rahnamayan, Hamid R. Tizhoosh, Magdy M.A. Salama,
    "A novel population initialization method for accelerating evolutionary
    algorithms" - Computers & Mathematics with Applications
    Volume 53, Issue 10, 2007, Pages 1605-1614, ISSN 0898-1221
    '''

    a, b = 0, 0
    for i, val in enumerate(x):
        a += val**2
        b += 0.5*i*val
    return a + b**2 + b**4





class tsp():
    def __init__(self, dist_func, close_loop=True):
        self.dist_func = dist_func
        self.close_loop = close_loop

    def dist(self, xy):
        # sequentially calculate distance between all tsp nodes
        dist = 0
        for i in range(len(xy)-1): dist += self.dist_func(xy[i+1], xy[i])

        # close the tsp loop by calculating the distance
        # between the first and last points
        if self.close_loop: dist += self.dist_func(xy[0], xy[-1])

        return dist


#--- END ----------------------------------------------------------------------+
