import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

def func(x, a, b):
    return a*x + b

a = ufloat(4.789, 0.001) * 10**(-3)
b = ufloat(72.3, 0.4)

s = ( func(550, a, b) - func(450, a, b) ) / ( func(500, a, b) )

print(s * 100)
print("-----------------------------------------")

n1 = ufloat(12914, 114)  / 60
n2 = ufloat(15790, 126)  / 60
n12 = ufloat(27965, 167) / 60

T = (n1 + n2 - n12)/(2*n1*n2)

print(T*10**4)

print("-----------------------------------------")

I = np.array([0.2, 0.4, 0.6]) * 10**(-6)
Z = [ufloat(11045, 105), ufloat(11174, 106), ufloat(11444, 107)]
t = 150

for i in range(0, 3):
    print(I[i] * t / Z[i] * 10**9)
    print(I[i] * t / Z[i] / ( 1.602176634 * 10**(-19)))