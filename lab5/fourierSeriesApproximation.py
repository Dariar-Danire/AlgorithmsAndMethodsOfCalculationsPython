import math
import matplotlib.pyplot as pyplot
from lab5.integrator import integral
from lab5.generateX import generateX
def f(x):
    return abs(math.cos(x))

def fourierSeriesApproximation(func, N, x, T):
    a0 = 2/T * integral(f, 0, T)
    res = a0/2

    for i in range(1, N + 1):
        a = 2/T * integral(lambda first: func(first) * math.cos(i * first), 0, T)
        b = 2/T * integral(lambda second: func(second) * math.sin(i * second), 0, T)

        res += a * math.cos(i * x) + b * math.sin(i * x)

    return res

def solve():
    print("Введите число гармоник:")
    N = int(input())

    x = generateX()
    T = 2 * math.pi

    y_approximated = []
    for i in range(len(x)):
        y_approximated.append(fourierSeriesApproximation(f, N, x[i], T))

    y = []
    for i in range(len(x)):
        y.append(f(x[i]))

    pyplot.grid()
    pyplot.plot(x, y_approximated, marker='o', markersize=2)
    pyplot.show()