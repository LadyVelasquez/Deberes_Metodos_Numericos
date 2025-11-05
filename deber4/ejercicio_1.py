import math

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)
    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            return p, i
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return None, i

TOL = 1e-2
N0 = 100

raiz_a, it_a = biseccion(f, 0.0, 1.0, TOL, N0)
raiz_b, it_b = biseccion(f, 1.0, 3.2, TOL, N0)
raiz_c, it_c = biseccion(f, 3.2, 4.0, TOL, N0)

print(f"El resultado de la bisección en [0, 1] da la raíz {raiz_a} en {it_a} iteraciones")
print(f"El resultado de la bisección en [1, 3.2] da la raíz {raiz_b} en {it_b} iteraciones")
print(f"El resultado de la bisección en [3.2, 4] da la raíz {raiz_c} en {it_c} iteraciones")
