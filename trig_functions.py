import numpy as np
import math
import matplotlib.pyplot as plt
def sin_(x, err):
    x = x%(2*np.pi)
    s1,s2 = 0,0

    for i in range(10000):
        s2 = s1
        s1 += float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if s2 != 0:
            if (abs(s2-s1)/abs(s2)) <= err:
                break
    return s1
def cos_(x, err):
        x = x%(2*np.pi)
        s1,s2 = 0,0

        for i in range(10000):
            s2 = s1
            s1 += float((((-1)**i) * (x**(2*i))))/float(math.factorial(2*i))
            if s2 != 0:
                if (abs(s2-s1)/abs(s2)) <= err:
                    break
        return s1
def tan_(x):
    if cos_(x) == 0:
        return "The tangent is undefined"
    else:
        return sin_(x)/cos_x(x)
def sec_(x):
    if cos_(x) == 0:
        return "The secant is undefined"
    else:
        return 1/cos_(x)
def cosec_(x):
    if sin_(x) == 0:
        return "The cosecant is undefined"
    else:
        return 1/sin_(x)

x = np.linspace(0, 2*np.pi, 100)
