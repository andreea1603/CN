def f(x, fun):
    fun = [1/3, -2, 2, 3]
    fun = [1, -6, 13, -12, 4]
    fx = 0
    for i in range(0, len(fun)):
        fx = fx + x**(len(fun)-i-1)*fun[i]
    return fx
k1 = -1
k2 = -1

def g1(fun, x):
    h = 10**-6
    value = (3*f(x,fun) - 4*f(x-h, fun) + f(x-2*h, fun))/(2*h)
    return value


def g2(fun, x):
    h = 10**-6
    value = (-f(x+2*h, fun)+8*f(x+h, fun)-8*f(x-h,fun)+f(x-2*h,fun))/(12*h)
    return value


def f2(fun, x):
    h = 10**-6
    val = (-f(x+2*h, fun)+16*f(x+h, fun) - 30*f(x, fun)+ 16*f(x-h, fun) - f(x-2*h, fun))/(12*h*h)
    return val


def deltag1(x, fun):
    g_x = g1(fun, x)
    delta_g1 = g_x*g_x/(g1(fun, x+g_x)-g_x)
    return delta_g1


def deltag2(x, fun):
    g_x = g2(fun, x)
    delta_g2 = g_x*g_x/(g2(fun, x+g_x)-g_x)
    return delta_g2


def steffensen(x0, fun):
    global k1
    x = x0
    k1 = 0
    eps = 10**-6
    k_max = 1000
    ok = 0
    x_d =0
    while ok ==0 or (eps <= x_d <= 10 ** 8 and k1 <= k_max):
        if ok == 0:
            ok = 1
        g_x = g2(fun, x)
        value = abs(g2(fun, x+g_x)-g_x)
        if value <= eps:
            print(x)
            return x
        x_d = deltag2(x, fun)
        x = x - x_d
        k1 = k1 + 1

    if k1<k_max and f2(fun, x)>0 and abs(deltag2(x,fun))<= eps:
        print(x)
        return x
    return -1


def steffensen1(x0, fun):
    x = x0
    global k2
    k2 = 0
    eps = 10**-6
    k_max = 1000
    ok = 0
    x_d =0
    while ok ==0 or (eps <= x_d <= 10 ** 8 and k2 <= k_max):
        if ok == 0:
            ok = 1
        g_x = g1(fun, x)
        value = abs(g1(fun, x+g_x)-g_x)
        if value <= eps:
            print(x)
            k2 = k2 + 1
            return x
        x_d = deltag1(x, fun)
        x = x - x_d
        k2 = k2 + 1

    if k2<k_max and f2(fun, x)>0 and abs(deltag1(x,fun))<= eps:
        print(x)
        return x
    return -1


if __name__ == '__main__':
    i = -1
    while i <= 10:
        sol1 = steffensen(i,"")
        # print("Solutia e : ",sol1)
        # print("Am iesit cu k = ", k1)
        sol2 = steffensen1(i,"")

        if k1!=0 and k2!=0 and k1!=1001 and k2!=1001 and sol1!=-1 and sol2!=-1:
            print("x0 = ", i)
            print("Diferenta: ", k1 - k2)
        else:
            if k1!=0 and k1!=1001 and sol1!=-1:
                print("x0 = ", i)
                print("K iteratii pentru metoda 1: ", k1)
            if k2!=0 and k2!=1001 and sol2!=-1:
                print("x0 = ", i)
                print("K iteratii pentru metoda 2: ", k2)
        i = i + 1
