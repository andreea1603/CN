import time
from collections import defaultdict


def update(array, a):
    for i in range(0, len(array)):
        if array[i][1]==a[0]:
            return a[0] + array[i][0]


def memMatrix(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    matrix = []
    dictionar = dict()
    for i in range(0, int(Lines[0])):
        matrix.append([])
    for line in Lines:
        line = line.rstrip("\n")
        elem = line.split((', '))
        if len(elem) == 3:
            if int(elem[1]) >= int(elem[2]) and float(elem[0])!= 0:
                try:
                    if exists(matrix[int(elem[1])], int(elem[2])):
                        matrix[int(elem[1])] = update(matrix[int(elem[1])], ((float(elem[0]), int(elem[2]))))
                except Exception as e:
                    print("Nu exista")
                matrix[int(elem[1])].append((float(elem[0]), int(elem[2])))
    return matrix


def memdict(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    matrix = []
    dictionar = dict()
    for i in range(0, int(Lines[0])):
        matrix.append([])
    for line in Lines:
        line = line.rstrip("\n")
        elem = line.split((', '))
        if len(elem) == 3:
            # elem[0] --> valoare, elem[1] --> i, elem[2] --> j
            if int(elem[1]) >= int(elem[2]) and float(elem[0]) != 0:
                try:
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

def get(A, j):
    try:
        for i in range(0, len(A)):
            if A[i][1]==j:
                return A[i][0]
    except Exception as e:
        return 0
    return 0

def get2(A, i, j):
    try:
        for k in range(0, len(A[i])):
            if A[i][k][1] == j:
                return A[i][k][0]
    except Exception as e:
        print(e)
        return 0

    return 0

def exists(array, a):
    for i in range(0, len(array)):
        if array[i][1] == a:
            return True
    return False


def addMatrix(a, b):
    c = []
    for i in range(0, len(a)):
        c.append([])
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if exists(a[i], j) or exists(b[i], j):
                if (get(a[i], j) + get(b[i], j))!= 0:
                    c[i].append(((get(a[i], j) + get(b[i], j)), j))
                else:
                    print(get(a[i], j) ,  get(b[i], j))
    return c


def verify_equality(matrix_1, matrix_2):
    find = True
    num = 0
    eps = 10**-3
    num2 = 0
    for i in range(0, len(matrix_1)):
        for k in matrix_1[i]:
            for j in matrix_2[i]:
                if abs(j[1] - k[1])<= eps:
                    if abs(j[0] - k[0]) > eps:
                        num = num + 1
                        if num > 300:
                            find = False
                            break
                    else:
                        num2= num2 + 1
            if not find:
                break
        if not find:
            break
    return find


def checkMul(matrix_1, matrix_2):
    eps = 10**-3
    for i in range(0, len(matrix_1)):
        for j in range(0, i+1):
            try:
                if abs(matrix_1[i][j]-matrix_2[i][j]) > eps:
                    return False
            except Exception as e:
                pass
    return True



def mulMatrix5(a):
    rez = {}

    for l1 in a.keys():
        if a[l1]!=0:
            for c1 in a[l1].keys():
                if a[l1][c1]!=0:
                    for l2 in a.keys():
                            for c2 in a[l2].keys():
                                if l1<l2 or (l1==l2 and c1<=c2):
                                    if a[l2][c2]!=0:
                                        if l1 == l2 and c1 == c2:
                                            if rez.get(l1):
                                                if rez.get(l1).get(l2):
                                                    rez[l1][l2] = rez.get(l1).get(l2) + a[l1][c1]* a[l1][c1]
                                                else:
                                                    rez[l1][l2] = a[l1][c1] * a[l1][c1]
                                            else:
                                                rez[l1] = {l2: a[l1][c1]* a[l1][c1]}
                                            if rez.get(c1) :
                                                if rez.get(c1).get(c2):
                                                    rez[c1][c2] = rez.get(c1).get(c2) + a[l1][c1]* a[l1][c1]
                                                else:
                                                    rez[c1][c2] = a[l1][c1] * a[l1][c1]
                                            else:
                                                rez[c1] = {c2: a[l1][c1]* a[l1][c1]}
                                        elif l1 == l2:
                                            #primul elem mai mare, mare: {mic: } k >= j si l >=i
                                            # l1<=l2 and c1<=c2
                                            if rez.get(c2):
                                                if rez.get(c2).get(c1):
                                                    rez[c2][c1] = rez.get(c2).get(c1) + a[l1][c1] * a[l2][c2]
                                                else:
                                                    rez[c2][c1] = a[l1][c1]* a[l2][c2]
                                            else:
                                                rez[c2] = {c1: a[l1][c1] * a[l2][c2]}
                                        elif c2 == c1:
                                            if rez.get(l2):
                                                if rez.get(l2).get(l1):
                                                    rez[l2][l1] = rez.get(l2).get(l1) + a[l1][c1] * a[l2][c2]
                                                else:
                                                    rez[l2][l1] = a[l1][c1] * a[l2][c2]
                                            else:
                                                rez[l2] = {l1: a[l1][c1] * a[l2][c2]}
                                        elif l1==c2:
                                            # primul elem mai mare, mare: {mic: } k >= j si l >=i
                                            # l1<=l2 and c1<=c2
                                            if rez.get(l2):
                                                if rez.get(l2).get(c1):
                                                    rez[l2][c1] = rez.get(l2).get(c1) + a[l1][c1] * a[l2][c2]
                                                else:
                                                    rez[l2][c1] = a[l1][c1] * a[l2][c2]
                                            else:
                                                rez[l2] = {c1: a[l1][c1] * a[l2][c2]}
    for i in range(0, len(a)+1):
        if rez.get(i):
            if rez.get(i).get(i):
                if a.get(i):
                    if a.get(i).get(i):
                        rez[i][i] = rez[i][i] - a[i][i]*a[i][i]
    f = open("rez.txt", "a")
    f.truncate(0)
    f.write(rez.__str__())
    f.close()
    return rez


a = memMatrix("a.txt")
b = memMatrix("b.txt")
aDict = memdict("a.txt")

print(time.localtime())
c = addMatrix(a, b)
a_plus_b = memMatrix("a_plus_b.txt")
print(verify_equality(c, a_plus_b))

print(time.localtime())

multiply = mulMatrix5(aDict)
a_ori_a = memdict("a_ori_a.txt")
print(checkMul(multiply, a_ori_a))
print(time.localtime())
