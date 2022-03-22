# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import math
import time

d = []
def exists(array, a):
    for i in range(0, len(array)):
        if array[i][1] == a:
            return True
    return False

def update(array, a):
    for i in range(0, len(array)):
        if array[i][1]==a[0]:
            return a[0] + array[i][0]


def memdict(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    matrix = []
    dictionar = dict()
    global d
    for i in range(0, int(Lines[0])):
        matrix.append([])
    k = 0
    for line in Lines:

        line = line.rstrip("\n")
        elem = line.split((', '))
        if k == 0:
            d = [0]*(int(line))
            k = k + 1
        if len(elem) == 3:
            # elem[0] --> valoare, elem[1] --> i, elem[2] --> j
            if int(elem[1]) >= int(elem[2]) and float(elem[0]) != 0:
                try:
                    if int(elem[1]) == int(elem[2]):
                        d[int(elem[2])] = float(elem[0])
                    if exists(matrix[int(elem[1])], int(elem[2])):
                        matrix[int(elem[1])] = update(matrix[int(elem[1])], ((float(elem[0]), int(elem[2]))))
                        dictionar[int(elem[1])][int(elem[1])] = dictionar[int(elem[1])][int(elem[1])] + float(elem[0])
                    else:
                        matrix[int(elem[1])].append((float(elem[0]), int(elem[2])))
                        if not dictionar.get(int(elem[1])) is not None:

                            dictionar[int(elem[1])] = {int(elem[2]): float(elem[0])}
                        else:
                            dictionar[int(elem[1])][int(elem[2])] =  float(elem[0])
                except Exception as e:
                    print(e)

    return dictionar


def verif_diag(a):
    k = 0
    for i in a.keys():
        for j in a[i].keys():
            if i == j:
                if a.get(i).get(j):
                    k = k + 1
    return (k==len(a))


def checksolution(a, b, x):
    dif = [0]*len(b)
    rez = [0]*len(b)
    for l1 in a.keys():
        for c1 in a[l1].keys():
            if a[l1][c1] !=0:
                for c2 in range(0, len(x)):
                    if l1 == c2 and c2 == c1:
                        dif[c2] = dif[c2] + a[l1][c1] * x[c2]
                    elif l1 == c2:
                        dif[c1] = dif[c1] + a[l1][c1] * x[c2]
                    elif c1 == c2:
                        dif[l1] = dif[l1] + a[l1][c1] * x[c2]
    val = infinit_norm(b, dif)
    return val


def infinit_norm(matrix, b):
    max_val = 0
    for i in range(len(b)):
        val = matrix[i] - b[i]
        if abs(val) > max_val:
            max_val = abs(val)
    return max_val


def delta(xc, xp):
    norma = 0
    for i in range(0, len(xc)):
        norma = norma + (xc[i]-xp[i])*(xc[i]-xp[i])
    return math.sqrt(norma)


def sumc(a, i, x):
    sum = 0
    global d
    for j in range(0, len(a)):
            if a.get(i).get(j) and x[j]:
                sum = sum + a.get(i).get(j)* x[j]
            elif a.get(j).get(i) and x[j]:
                sum = sum + a.get(j).get(i) * x[j]
    sum = sum - d[i]*x[i]
    return sum



def iacobi(a, b):
    xp = [0]*len(b)
    xc = [0]*len(b)
    k = -1
    eps = 10**-6
    kmax = 10000
    # Xc --> x current ; Xp --> x Precedent
    norma = 0
    while k==-1 or (norma>=eps and k <= kmax and norma<=10**8):
        xp = copy.deepcopy(xc)
        for i in range(0, len(b)):
            xc[i] = b[i] - sumc(a, i, xp)
            xc[i] = xc[i] /a.get(i).get(i)
        norma = delta(xp, xc)
        k = k + 1
    print("Numarul de iteratii facute: ",k)

    return xc


def memvect(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    b = []
    for line in Lines:
        line = line.rstrip("\n")
        b.append(float(line))
    return b


if __name__ == '__main__':

    a = memdict("text.txt")
    b = memvect("testb.txt")

    print(time.localtime())
    sol = iacobi(a, b)
    print(time.localtime())
    print("3. Norma infinit:", checksolution(a, b, sol))

    print(time.localtime())
    a_5 = memdict("a_5.txt")
    b_5 = memvect("b_5.txt")
    if verif_diag(a_5):
        sol = iacobi(a_5, b_5)
        print("3. Norma infinit:", checksolution(a_5, b_5, sol))

    print(time.localtime())
    a_3 = memdict("a_3.txt")
    b_3 = memvect("b_3.txt")
    if verif_diag(a_3):
        sol = iacobi(a_3, b_3)
        print("3. Norma infinit:", checksolution(a_3, b_3, sol))

    print(time.localtime())
    a_2 = memdict("a_2.txt")
    b_2 = memvect("b_2.txt")
    if verif_diag(a_2):
        sol = iacobi(a_2, b_2)
        print("3. Norma infinit:", checksolution(a_2, b_2, sol))

    print(time.localtime())
    a_4 = memdict("a_4.txt")
    b_4 = memvect("b_4.txt")
    if verif_diag(a_4):
        sol = iacobi(a_4, b_4)
        print("3. Norma infinit:", checksolution(a_4, b_4, sol))


    print(time.localtime())
    a_1 = memdict("a_1.txt")
    b_1 = memvect("b_1.txt")
    if verif_diag(a_1):
        sol = iacobi(a_1, b_1)
        print("3. Norma infinit:", checksolution(a_1, b_1, sol))
