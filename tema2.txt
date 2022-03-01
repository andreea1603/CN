import copy
import math
import random

import numpy


def switchLines(a, l, c, b):
    temp = a[l]
    a[l] = a[c]
    a[c] = temp
    temp = b[l]
    b[l]= b[c]
    b[c] = temp
    return [a, b]


def getPivot(i, a):
    max = a[i][i]
    line = -1
    col = -1
    for j in range(i, len(a)):
        if a[j][i] > max:
            max = a[j][i]
            line = j
            col = i
    return [line, col]


def Gauss(a, b):
    l = 0
    line, col = getPivot(0, a)
    if line!= l :
        a,b = switchLines(a, l, line, b)
    eps = 10**-6
    c = 1
    n = len(a)
    b1= b
    a1 = a
    while l < n -1 and abs(a[l][l]) > eps and c < 20:
        c = c + 1
        for i in range(0, n):
            for j in range(0, n):
                a1[i][j]= a[i][j]
        for i in range(0, n):
            b1[i] = b[i]
        for i in range(l+1, n):
            for j in range(l+1, n):
                a1[i][j] = a[i][j] - a[i][l]/a[l][l]*a[l][j]
            for i in range(l+1, n):
                b1[i]= b[i] - a[i][l]/a[l][l]*b[l]
                a1[i][l]= 0
        l = l +1
        line, col = getPivot(l, a)
        if line!= l:
            a,b = switchLines(a, l, line, b)
        print(a)
    if abs(a[l][l]) <= eps:
        print("matrice singulara")
        return True
    else:
        print("matrice nesingulara")
        return False


def solve(a, b):
    if Gauss(a, b) == False:
        n = len(a)
        x = [0]*(n)
        for i in range(n-1, -1, -1):
            sum = 0
            for j in range(i+1, n):
                   sum = sum + a[i][j]*x[j]
            value = b[i] - sum
            if a[i][i] == 0:
                x[i] = value / (10 ** -6)
            else:
                x[i] = value / a[i][i]
        #print(x)
        return x


def euclidean(rez):
    sum = 0
    #print(rez)
    for i in range(0, len(rez)):
        sum = sum + rez[i]* rez[i]
    print("Diferenta:", math.sqrt(sum))


def checkSolution(a, b, x):

    rez = [0]*len(b)
    n= len(a)
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + a[i][j]* x[j]
        rez[i] = sum
    dif = [0]*len(b)
    for i in range(0, len(b)):
        dif[i] = rez[i] - b[i]
    euclidean(dif)


def solutionLib(A, B):
    X = numpy.linalg.solve(A,B)
    #print("Solutie X lib:", X)
    return X


def invertLib(A):
    A1= numpy.linalg.inv(A)
    return A1


def XgaussXbibl(Xg, Xb):
    rez= [0]*len(Xb)
    for i in range(0, len(Xg)):
        rez[i] = Xg[i]- Xb[i]
    sum = 0
    for i in range(0, len(Xb)):
        sum = sum + rez[i]* rez[i]
    return math.sqrt(sum)


def XgaussABbibl(A, B, Xg):
    rez = invertLib(A).dot(B)
    return XgaussXbibl(Xg, rez)


def GaussI(a, b, aInit):
    l = 0
    line, col = getPivot(0, a)
    if line!= l :
        a,b = switchLines(a, l, line, b)
    eps = 10**-6
    c = 1
    n = len(a)
    b1= b
    a1 = a
    m = len(a[0])
    while l < n -1 and abs(a[l][l]) > eps:
        for i in range(0, n):
            for j in range(0, m):
                a1[i][j]= a[i][j]
        for i in range(0, n):
            b1[i] = b[i]
        for i in range(l+1, n):
            for j in range(l+1, m):
                a1[i][j] = a[i][j] - a[i][l]/a[l][l]*a[l][j]
        for i in range(l+1, n):
            b1[i]= b[i] - a[i][l]/a[l][l]*b[l]
            a1[i][l]= 0
        l = l +1
        line, col = getPivot(l, a)
        if line!= l:
            a,b = switchLines(a, l, line, b)

    rez = copy.deepcopy(aInit)
    for i in range(0, len(aInit)):
        for j in range(0, len(aInit)):
            rez[i][j]= a[i][j]

    iTrans = copy.deepcopy(aInit)
    for i in range(0, len(aInit)):
        for j in range(0, 3):
            iTrans[j][i] = a[i][j+ len(aInit)]
    return [rez, iTrans]


def solve1(a, b):
        n = len(a)
        x = [0]*(n)
        for i in range(n-1, -1, -1):
            sum = 0
            for j in range(i+1, n):
                   sum = sum + a[i][j]*x[j]
            value = b[i] - sum
            if a[i][i] == 0:
                x[i] = value / (10**-6)
            else:
                x[i] = value/a[i][i]
        return x


def getA_In(a):
    rez = copy.deepcopy(a)
    In = copy.deepcopy(a)
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i == j :
                In[i][j] = 1
            else:
                In[i][j]= 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            rez[i].append(In[i][j])
    return rez


def transpusa(a):
    transpusa = copy.deepcopy(a)
    for i in range(0, len(a)):
        for j in range(0, len(a)):
           transpusa[j][i] = a[i][j]
    return transpusa


def generateMatrix(n):
    matrix = []
    for i in range(0, n):
        values = generateB(n)
        matrix.append(values)
    print(matrix)
    return matrix


def generateB(n):
    values = []
    for j in range(0, n):
        values.append(random.randint(0, 100))
    return values


if __name__ == '__main__':
    a = [[2,0.5, 2], [4, 3, 8], [0, 2, 6]]
    b = [4.5, 11, 2]
    # a = generateMatrix(100)
    # b = generateB(100)
    aCopy = copy.deepcopy(a)
    bCopy = copy.deepcopy(b)
    getA_In(a)
    a1 = copy.deepcopy(a)
    b1 = copy.deepcopy(b)
    print("A)")
    x = solve(a, b)
    print("B)")
    checkSolution(a1, b1, x)
    print("C)")
    xl = solutionLib(a1, b1)
    print("Inversa A ", invertLib(a1))
    a_1lib = copy.deepcopy(invertLib(a1))
    print("Norma Xgauss, Xbibl ", XgaussXbibl(x, xl))
    print("Norma Xgauss, A-1bibl * binit",XgaussABbibl(a1, b1, x))

    print("D)")
    ai= getA_In(aCopy)
    R, bModif = GaussI(ai, bCopy, aCopy)

    a_1 = []
    for i in range(0,len(bModif)):
        a_1.append(solve1(R, bModif[i]))
    print("A la -1: ",transpusa(a_1))

    print("Norma Alib-1, Agauss -1 : ", numpy.linalg.norm(numpy.subtract(a_1lib,invertLib(a1))))
