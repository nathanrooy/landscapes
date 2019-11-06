#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   Nov. 2019
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from math import cos
from math import sin
from math import pi
from math import exp
from math import sqrt
from math import e

#--- FUNCTIONS ----------------------------------------------------------------+

def rastrigin(x, safe_mode=False):
    '''
    Rastrigin Function
    
    wikipedia: https://en.wikipedia.org/wiki/Rastrigin_function

    global minimum at x=0, where f(x)=0
    bounds: -5.12 <= x_i <= 5.12
    '''
    if safe_mode:
        for item in x: assert x<=5.12 and x>=-5.12, 'input exceeds bounds of [-5.12, 5.12]'
    return len(x)*10.0 +  sum([item*item - 10.0*cos(2.0*pi*item) for item in x])


def ackley(xy):
    '''
    Ackley Function
    
    wikipedia: https://en.wikipedia.org/wiki/Ackley_function
    
    global minium at f(x=0, y=0) = 0
    bounds: -5<=x,y<=5
    '''
    x=xy[0]
    y=xy[1]
    return (-20 * exp(-0.2 * sqrt(0.5 * (x*x + y*y))) -
            exp(0.5 * (cos(2.0*pi*x) + cos(2*pi*y))) + e + 20)


def sphere(x):
    '''
    Sphere Function
    
    global minimum at x=0 where f(x)=0
    bounds: none
    '''
    return sum([item * item for item in x])


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


def goldstein_price(xy):
    '''
    Goldstein-Price Function

    global minimum: f(0, -1) = 3
    bounds: -2 <= x, y <= 2
    '''
    x, y = xy[0], xy[1]
    return ((1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) *
            (30 + (2*x-3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)))


def booth(x,y):
    '''
    Booth Function

    global minimum: f(x=1, y=3) = 0
    bounds: 10 <= x, y <= 10
    '''
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2


def bukin_n6(x,y):
    '''
    Bukin Function N.6

    global minimum: f(x=-10, y=1) = 0
    bounds:
        -15 <= x <= -5
        -3 <= y <= 3
    '''
    return 100 * sqrt(abs(y-0.01*x**2)) + 0.01*abs(x+10)


def matyas(x,y):
    '''
    Matyas Function

    global minimum: f(x=0, y=0) = 0
    bounds: -10 <= x, y <= 10
    '''
    return 0.26*(x**2 + y**2) - 0.48*x*y


def levi_n13(x,y):
    '''
    Levi Function N.13

    global minimum: f(x=1, y=1) = 0
    bounds: -10 <= x, y <= 10
    '''
    return sin(3.0*pi*x)**2 + (x-1)**2 * (1+sin(3.0*pi*y)**2) + (y-1)**2 * (1+sin(2.0*pi*y)**2)


def himmelblau(x,y):
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
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def three_hump_camel(x,y):
    '''
    Three-Hump Camel Function

    global minimum: f(x=0, y=0) = 0
    bounds: -5 <= x, y <= 5
    '''
    return 2.0*x**2 - 1.05*x**4 + (x**6 / 6.0) + x*y + y**2


def easom(x,y):
    '''
    Easom Function

    global minimum: f(x=pi, y=pi) = -1
    bounds: -100 <= x, y <= 100
    '''
    return -cos(x)*cos(y)*exp(-((x-pi)**2 + (y-pi)**2))


def cross_in_tray(x,y):
    '''
    Cross-in-tray Fucntion

    global minimum:
        f(x=1.34941, y=1.34941) = -2.06261
        f(x=1.34941, y=-1.34941) = -2.06261
        f(x=-1.34941, y=1.34941) = -2.06261
        f(x=-1.34941, y=-1.34941) = -2.06261
    bounds: -10 = x, y <= 10
    '''
    return -0.0001*(abs(sin(x)*sin(y)*exp(abs(100-(sqrt(x**2 + y**2)/pi))))+1)**0.1


def eggholder(xy):
    '''
    Eggholder Function

    global minimum: f(x=512, y=404.2319) = -959.6407
    bounds: -512 <= x, y <= 512
    '''
    x, y = xy[0], xy[1]
    return (-(y+47)*sin(sqrt(abs((x/2.0) + (y+47)))) -
            x*sin(sqrt(abs(x-(y+47)))))


def holder_table(x,y):
    '''
    Holder Table Function

    global minimum:
        f(x= 8.05502, y= 9.66459) = -19.2085
        f(x=-8.05502, y= 9.66459) = -19.2085
        f(x= 8.05502, y=-9.66459) = -19.2085
        f(x=-8.05502, y=-9.66459) = -19.2085
    bounds: -10 <= x, y <= 10
    '''
    return -abs(sin(x)*cos(y)*exp(abs(1-(sqrt(x**2 + y**2)/pi))))


def mccormick(x,y):
    '''
    McCormick Function

    global minimum: f(x=-0.54719, y=-1.54719) = -1.9133
    bounds:
        -1.5 <= x <= 4
        -3 <= y <= 4
    '''
    return sin(x+y) + (x-y)**2 - 1.5*x + 2.5*y + 1


def schaffer_n2(x,y):
    '''
    Schaffer Function N.2

    global minimum: f(x=0, y=0) = 0
    bounds: -100 <= x, y <= 100
    '''
    return 0.5 + (sin(x**2 - y**2)**2 - 0.5)/(1+0.001*(x**2+y**2))**2


def schaffer_n4(x,y):
    '''
    Schaffer Function N.4

    global minimum:
        f(x=0, y= 1.25313) = 0.292579
        f(x=0, y=-1.25313) = 0.292579
    bounds: -100 <= x, y <= 100
    '''
    return 0.5 + (cos(sin(abs(x**2 - y**2)))**2 - 0.5)/(1+0.001*(x**2 + y**2))**2


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


#--- END ----------------------------------------------------------------------+
