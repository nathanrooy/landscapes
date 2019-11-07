<p  align="center"><img src="https://raw.githubusercontent.com/nathanrooy/landscapes/master/logo.png"></p>

[![GitHub license](https://img.shields.io/github/license/nathanrooy/landscapes.svg)](https://github.com/nathanrooy/landscapes/blob/master/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/landscapes.svg)](https://pypi.python.org/pypi/landscapes/)
[![PyPI version fury.io](https://badge.fury.io/py/landscapes.svg)](https://pypi.python.org/pypi/landscapes/)
[![Downloads](https://pepy.tech/badge/landscapes)](https://pepy.tech/project/landscapes)

## Installation
There are a couple ways in which you can use this library. The first and probably the easiest is by using pip and PyPi:
```sh
pip install landscapes
```
You can also install directly from this git repo:
```sh
pip install git+https://github.com/nathanrooy/landscapes
```
Lastly, you can always clone/download this repo and use as is.
```sh
wget https://github.com/nathanrooy/landscapes/archive/master.zip
unzip master.zip
cd landscapes-master
```

## Usage

As a simple example, let's use the <a target="_blank" href="https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method">Nelder-Mead method</a> via <a target="_blank" href="https://www.scipy.org/">SciPy</a> to minimize the sphere function. We'll start off by importing the `sphere` function from Landscapes and the `minimize` method from SciPy.
```py
>>> from landscapes.single_objective import sphere
>>> from scipy.optimize import minimize
```
Next, we'll call the `minimize` method using a starting location of [5,5].
```py
>>> minimize(sphere, x0=[5,5], method='Nelder-Mead')
```
The output of which should look close to this:
```py
 final_simplex: (array([[-3.33051318e-05, -1.93825710e-05],
       [ 4.24925225e-05,  1.37129516e-05],
       [ 3.09383247e-05, -4.04797876e-05]]), array([1.48491586e-09, 1.99365951e-09, 2.59579314e-09]))
           fun: 1.4849158640215086e-09
       message: 'Optimization terminated successfully.'
          nfev: 80
           nit: 44
        status: 0
       success: True
             x: array([-3.33051318e-05, -1.93825710e-05])

```
