import copy
import math
import numpy
import numpy as np
from numpy.linalg import eig, svd, matrix_rank, cond, pinv
from scipy.linalg import pinvh


def getIn(a, n):
    In = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        In[i][i] = 1
    return In


def rAr(a, c, s, t, p, q):
    for j in range(0, len(a)):
        if j != p and j != q:
            a[p][j] = c * a[p][j] + s * a[q][j]
            a[q][j] = a[j][q] = -s * a[j][p] + c * a[q][j]
            a[j][p] = a[p][j]
    a[p][p] = a[p][p] + t * a[p][q]
    a[q][q] = a[q][q] - t * a[p][q]
    a[p][q] = a[q][p] = 0
    return a


def f7(u, p, q, c, s):
    uVeche = copy.deepcopy(u)
    for i in range(0, len(u)):
        u[i][p] = c * u[i][p] + s * u[i][q]
        u[i][q] = -s * uVeche[i][p] + c * u[i][q]
    return u


def getIndexes(a):
    max = a[0][1]
    p = 0
    q = 1
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if abs(a[i][j]) > max:
                p = i
                q = j
                max = abs(a[i][j])
    return p, q


def isDiagonal(a):
    eps = 10 ** -7
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i != j and abs(a[i][j]) > eps:
                return False
    return True


def compute(a):
    k = 0
    k_max = 1000
    U = getIn(a, len(a))
    p, q = getIndexes(a)
    alfa = (a[p][p] - a[q][q]) / (2 * a[p][q])
    if alfa >= 0:
        t = -alfa + math.sqrt(alfa * alfa + 1)
    else:
        t = -alfa - math.sqrt(alfa * alfa + 1)
    c = 1 / math.sqrt(1 + t * t)
    s = t / math.sqrt(1 + t * t)
    eps = 10**-6
    while not isDiagonal(a) and k <= k_max:
        a = rAr(a, c, s, t, p, q)
        U = f7(U, p, q, c, s)
        p, q = getIndexes(a)
        if abs(a[p][q]) > eps:
            alfa = (a[p][p] - a[q][q]) / (2 * a[p][q])
            if alfa >= 0:
                t = -alfa + math.sqrt(alfa * alfa + 1)
            else:
                t = -alfa - math.sqrt(alfa * alfa + 1)
            c = 1 / math.sqrt(1 + t * t)
            s = t / math.sqrt(1 + t * t)
            k = k + 1

    return a, U


def mul(a, u):
    A = numpy.array(a)
    B = numpy.array(u)
    return numpy.dot(A, B)


def getEigenBibli(a):
    A = numpy.array(a)
    w, v = eig(A)

    return w, v


def minLam(lj, lb):
    sum = 0
    for i in range(0, len(lj)):
        min = abs(lj[i] - lb[0])
        for k in range(0, len(lb)):
            if abs(lj[i] - lb[k]) < min:
                min = abs(lj[i] - lb[k])
        sum = sum + min
    print("Suma minimelor este: ", sum)


def diff(a, b):
    dif = copy.deepcopy(a)
    sum = 0
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            dif[i][j] = abs(a[i][j] - b[i][j])

    for i in range(0, len(dif)):
        for j in range(0, len(dif[i])):
            sum = sum + dif[i][j]
    print("\nDiferenta:", sum)


def computeRank(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] > 0:
            count = count + 1
    return count


def conditionNumber(s):
    maxi = mini = s[0]
    for i in range(0, len(s)):
        if s[i] > maxi:
            maxi = s[i]
        if s[i] < mini:
            mini = s[i]
    return maxi / mini


def ex3(a):
    Ub, sB, vtB = svd(a)
    print("U: ", Ub)
    print("S: ", sB)
    print("V: ", vtB)

    print("\nRangul matricei bibl este : ", matrix_rank(a))
    print("\nRangul matricei calcul este: ", computeRank(sB))
    print("\nNumarul de conditionare bibl este: ", cond(a))
    print("\nNumarul de conditionare calcul este: ", conditionNumber(sB))

    aI = pinv(a)
    print("\nMoore-Penrose pseudo-inversa: \n", aI)

    aTransp = np.transpose(a)
    aMul = np.dot(aTransp, a)
    aInv = np.linalg.inv(aMul)
    aJ = np.dot(aInv, aTransp)
    print("\nMatricea pseudo-inversa in sensul celor mai mici patrate\n")
    print(aJ)
    diff(aJ, aI)


def getEigenvalues(v):
    val = []
    for i in range(len(v) - 1, -1, -1):
        val.append(v[i][i])
    return val


if __name__ == '__main__':
    print("\b\033[1mExercitiul 1\033[0m\n")
    a = [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
    aInit = copy.deepcopy(a)
    a, U = compute(a)
    print("Eigenvectors by Jacobi: \n", U)
    print("Eigenvalues by Jacobi: \n ", getEigenvalues(a))
    print(diff(mul(aInit, U), mul(U, a)))

    print("\n\n\b\033[1mExercitiul 2\033[0m\n")
    ainit = [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
    w, v = getEigenBibli(ainit)
    print("Eigenvectors by bibl:",v)
    print("Eigenvalues by bibl:",w)

    minLam(w, getEigenvalues(a))

    print("\n\n\b\033[1mExercitiul 3\033[0m\n")
    aC = [[0, 0, 1], [0, 0, 1], [1, 1, 1], [1, 1, 1]]
    aC = [[-1, 3, 1], [0, 2, 1], [2, 2, 1], [2, 1, 1]]
    ex3(aC)
