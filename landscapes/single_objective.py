#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from math import cos
from math import pi

#--- FUNCTIONS ----------------------------------------------------------------+

def rastrigin(x, safe_mode=False):
    '''
    https://en.wikipedia.org/wiki/Rastrigin_function
    
    global minimum at x=0, where f(x)=0
    bounds: -5.12 <= x_i <= 5.12
    '''
    if safe_mode: 
        for item in x: assert x<=5.12 and x>=-5.12, 'input exceeds bounds of [-5.12, 5.12]'
    return len(x)*10.0 +  sum([item*item - 10.0*cos(2.0*pi*item) for item in x])
    
    
#--- END ----------------------------------------------------------------------+
