import numpy as np


class Integrator:
    def __init__(self, xMin, xMax, N):
        self._xmin = xMin
        self._xmax = xMax
        self._n = N
        self._dx = (xMax-xMin)/N
        self._val = 0

    def _func(self, x):
        # f(x)=x^2.e^−x.sin(x)
        return x**2*np.exp(-x)*np.sin(x)

    def integrate(self):
        for i in range(self._n):
            x_i = self._xmin + i*self._dx
            self._val += self._func(x_i) * self._dx

    def show(self):
        print(self._val)


examp = Integrator(1, 3, 200000)
examp.integrate()
examp.show()
