import math

def f(x):
    return x - 2 * math.sin(x)

def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)
    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            return p
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return None

raiz = biseccion(f, 1.5, 2.0, 1e-5, 100)
print(raiz)
