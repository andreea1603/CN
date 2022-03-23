def maxi(a):
    max = abs(a[0])
    for i in range(1, len(a)):
        if abs(a[i]) > max:
            max = abs(a[i])
    return max


def getR(a):
    R = (abs(a[0]) + maxi(a))/abs(a[0])
    return R


def delta(a, xk):
    try:
        p_k = pxk(a, xk)
        yk = xk - (2 * p_k * p_k) / (pxk(a, (xk + p_k)) - pxk(a, (xk - p_k)))

        delta = 2 * p_k * (p_k + pxk(a, yk))
        delta = delta / (pxk(a, (xk + p_k)) - pxk(a, (xk - p_k)))
    except Exception as e:
        print("hei, aici")
        return 0
    return delta


def pxk(a, x):
    b = a[0]
    for i in range(1, len(a)):
        b = a[i] + b * x
    return b


def dehghan(a, x0):
    eps = 10**(-4)
    kmax = 10000
    k = 0
    ok = 0
    x = x0
    xd = 0
    while ok==0 or (eps <= abs(xd) <= 10 ** 8 and k <= kmax):
        if ok == 0:
            ok = 1
        #calculam polinomul abs(xk) x0
        if abs(pxk(a, x)) <= eps/10:
            xd = 0
        else:
            xd = delta(a, x)
        x = x - xd
        k = k + 1
    if pxk(a, x) < 10**(-6):
        print("Delta este:" , xd)
        print(pxk(a, x))
        return x
    return "Divergenta"


def exists(vec, value):
    for i in range(0, len(vec)):
        if abs(vec[i]- value)<10**-2:
            return True
    return False


def resolve(a):
    r = getR(a)
    roots = []
    for i in range(int(-r), int(r)):
        rez = dehghan(a, i)
        if rez != "Divergenta":
            print(rez)
            if not exists(roots, rez):
                roots.append(rez)
    print(roots)
    f = open("rez.txt", "a")
    f.truncate(0)
    f.write(roots.__str__())
    f.close()

if __name__ == '__main__':
    #a = [1, -6, 13, -12, 4]
    a = [42, -55, -42, 49, -6]
    #a = [8, -38, 49, -22, 3]
    #a = [1, -6, 13, -12, 4]
    r = getR(a)
    print("[-R, R]: ", -r, r)
    resolve(a)
