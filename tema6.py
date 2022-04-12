import copy
import math

import numpy as np


def pxk(a, x):
    b = a[0]
    for i in range(1, len(a)):
        b = a[i] + b * x
    return b


def f3(x):
    return math.sin(x) - math.cos(x)


def f(k, x, y):
    sum = 0
    for i in range(0, k):
        prodx = 1
        for j in range(0, k):
            if i != j:
                prodx = prodx * (x[i] - x[j])
        sum = sum + y[i] / prodx
    return sum


def Ln(x, y, xf):
    val = y[0]
    for i in range(1, len(x)):
        term = 1
        for j in range(0, i):
            term = term * (xf - x[j])
        val = val + term * f(i + 1, x, y)
    print("Valoarea: ", val)
    return val


def ex1():
    # ex1
    a = [1, -12, 30]
    xf = 2

    print("Valoarea: ", pxk(a, xf))
    x = [1, 3, 4, 5]
    y = [19, 3, -2, -5]
    Ln(x, y, xf)
    print("Modulul diferentei",abs(Ln(x, y, xf) - pxk(a, xf)))

    # ex2
    print("\nEx 2")
    a = [2, 0, -3, 15]
    xf = 1.1
    print("Valoarea: ", pxk(a, xf))
    x = [0, 1, 2]
    y = [15, 14, 25]
    Ln(x, y, xf)
    print("Modulul diferentei",abs(Ln(x, y, xf) - pxk(a, xf)))
    # ex3
    print("\nEx3")
    xf = 1.4
    print(f3(xf))
    x = [0, 1, 1.5]
    y = [-1, 0.30116867893975674, 0.9267577849363515]
    Ln(x, y, xf)
    print("Modulul diferentei",abs(Ln(x, y, xf) - f3(xf)))


def getBij(m, x):
    b = [[0 for x in range(m)] for y in range(m)]
    for i in range(0, m):
        for j in range(0, m):
            b[i][j] = 0
            for k in range(0, len(x)):
                b[i][j] = x[k] ** (i + j) + b[i][j]
    return b


def getF(x, y, m):
    f = [0] * len(y)
    for i in range(0, m):
        for k in range(0, len(x)):
            f[i] = y[k] * (x[k] ** i) + f[i]
    return f


def ex2():
    xf = 2.2
    m = 4
    x = [1, 3, 4, 5]
    y = [19, 3, -2, -5]
    b = getBij(m, x)
    f = getF(x, y, m)
    # print(b)
    # print(f)
    a = np.linalg.solve(b, f)
    a1 = a[::-1]
    print("Valoare cele mai mici patrate: ", pxk(a1, xf))
    print("Valoare reala: ", pxk([1, -12, 30], xf))
    print("Modulul diferentei:", abs(pxk(a1, xf) - pxk([1, -12, 30], xf)))
    sum = 0
    for i in range(0, len(x)):
        sum = sum + abs(pxk(a1, x[i]) - pxk([1, -12, 30], x[i]))
    print("Diferenta intre valorile aflate si valorile stiute, reale",sum)
    print()

    # ex2
    m = 3
    x = [0, 1, 2]
    y = [15, 14, 25]
    xf = 1.2

    b = getBij(m, x)
    f = getF(x, y, m)
    # print(b)
    # print(f)
    a = np.linalg.solve(b, f)
    a1 = a[::-1]
    print("Valoare cele mai mici patrate: ", pxk(a1, xf))
    print("Valoare reala: ", pxk([2, 0, -3, 15], xf))
    print("Modulul diferentei:", abs(pxk(a1, xf) - pxk([2, 0, -3, 15], xf)))
    sum = 0
    for i in range(0, len(x)):
        sum = sum + abs(pxk(a1, x[i]) - pxk([2, 0, -3, 15], x[i]))
    print("Diferenta intre valorile aflate si valorile stiute, reale", sum)


if __name__ == '__main__':
    # x0 = input('Alegeti x0')
    # xn = input('Alegeti xn')
    print("\n\nEXERCITIUL 1\n\n")

    ex1()
    print("\n\nEXERCITIUL 2\n\n")
    ex2()
