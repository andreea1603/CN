import math
import random


def ex1():
    ok = True
    i = 1
    while ok:
        number = 1.0 + 10**(-1*i)
        if number == 1.0:
            ok = False
            return i-1
        i = i + 1


def ex2a():
    u = 1e-15
    a = 1.0
    b = u/10
    c = u/10
    if ((a+b)+c) != (a+(b+c)):
        print("Nu este asociativa")
        print("(a+b)+c): " , (a + b) + c)
        print("(a+(b+c): ", a + (b + c))


def findNumbers():
    counter = 0
    while counter < 10:
        counter = counter + 1
        a = random.random()
        b = random.random()
        c = random.random()
        if a * (b * c) != (a * b) * c:
            print("Not equal\n");
            print(a," ", b, ' ', c)


def ex2b():
    print("ex2b")
    u = 2**-100
    a = 0.5879631250075986
    b = 0.08505656477172963
    c = 0.36661125110393644
    if ((a*b)*c) != (a*(b*c)):
        print("Xc Nu este asociativa")
        print("(a*b)*c): " , (a * b) * c)
        print("(a*(b*c): ", a * (b * c))


def computePQ(x, a0, a1, a2, a3, a4, b0, b1, b2, b3, b4):
    y = x * x
    P4 = a0 + y*(a1 + y*(a2 + y*(a3 +y*a4)))

    Q4 = b0 + y*(b1 + y*(b2 + y*(b3 + y*b4)))
    if Q4 < 1e-12:
        Q4 = 1e-12
    return P4/Q4


def ex3Sinus(x):
    print("for sinus")
    a0 = 1805490264.690988571178600370234394843221
    a2 = 3664210.647581261810227924465160827365
    a4 = 76.568981088717405810132543523682
    a3 = -28904.140246461781357223741935980097
    a1 = -164384678.227499837726129612587952660511

    b0 = 2298821602.638922662086487520330827251172
    b1 = 27037050.118894436776624866648235591988
    b2 = 155791.388546947693206469423979505671
    b3 = 540.567501261284024767779280700089
    b4 = 1.0
    x1 = math.pi * 1 /4 * x

    rez = computePQ(x, a0, a1, a2, a3, a4, b0,b1, b2, b3, b4) * x
    print(rez)
    print(math.sin(x1))
    print(abs(rez - math.sin(x1)))


def ex3Cos(x):
    print("for cosinus")
    a0 =  1090157078.174871420428849017262549038606
    a1 = -321324810.993150712401352959397648541681
    a2 =  12787876.849523878944051885325593878177
    a3 = -150026.206045948110568310887166405972
    a4 =  538.333564203182661664319151379451

    b0 = 1090157078.174871420428867295670039506886
    b1 = 14907035.776643879767410969509628406502
    b2 = 101855.811943661368302608146695082218
    b3 =  429.772865107391823245671264489311
    b4 = 1.0
    x1 = math.pi * 1 /4 * x

    rez = computePQ(x, a0, a1, a2, a3, a4, b0,b1, b2, b3, b4)
    print(rez)
    print(math.cos(x1))
    print(abs(rez - math.cos(x1)))


def ex3ln(x):
    print("for ln")
    a0 = 75.151856149910794642732375452928
    a1 = -134.730399688659339844586721162914
    a2 = 74.201101420634257326499008275515
    a3 = -12.777143401490740103758406454323
    a4 = 0.332579601824389206151063529971
    b0 = 37.575928074955397321366156007781
    b1 = -79.890509202648135695909995521310
    b2 = 56.215534829542094277143417404711
    b3 = -14.516971195056682948719125661717
    b4 = 1.0

    z = (x -1)/(x + 1)
    rez = z * computePQ(z, a0, a1, a2, a3, a4, b0,b1, b2, b3, b4)
    print(rez)
    print(math.log(x))
    print(abs(rez - math.log(x)))


def ex2():
    ex2a()
    ex2b()


def ex3(x):
    if -1 <= x and x <=1:
        ex3Sinus(x)
        ex3Cos(x)
    else:
        print("X nu este in interval")
    if 1/math.sqrt(2) <=x and x <= math.sqrt(2):
        ex3ln(x)
    else:
        print("x nu este in interval")


def ex4(x):
    if -1 <= x and x <=1:
        ex3Sinus(x)
        ex3Cos(x)
    else:
        while -1 > x or x > 1:
            if x > 1:
                print(x)
            else:
                print(x)


if __name__ == '__main__':
    print("Exercitiul a")
    print(ex1())
    print("Exercitiul 2")
    ex2()
    print("Exercitiul 3")
    ex3Sinus(0.6)
    ex3Cos(0.6)
    ex3ln(2.7332)
