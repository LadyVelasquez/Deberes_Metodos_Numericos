import math

def f(x):
    return (x + 3) * (x + 1)**2 * (x - 1)**3 * (x - 3)

def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)
    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            return p  # éxito
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return None  # fracaso

TOL = 1e-5
N0 = 100

raiz_a = biseccion(f, -1.5, 2.5, TOL, N0)
raiz_b = biseccion(f, -0.5, 2.4, TOL, N0)
raiz_c = biseccion(f, -0.5, 3.0, TOL, N0)
raiz_d = biseccion(f, -3.0, -0.5, TOL, N0)

print("a) raíz aproximada en [-1.5, 2.5]:", f"{raiz_a:.5f}" if raiz_a is not None else "no convergió")
print("b) raíz aproximada en [-0.5, 2.4]:", f"{raiz_b:.5f}" if raiz_b is not None else "no convergió")
print("c) raíz aproximada en [-0.5, 3]:",   f"{raiz_c:.5f}" if raiz_c is not None else "no convergió")
print("d) raíz aproximada en [-3, -0.5]:",  f"{raiz_d:.5f}" if raiz_d is not None else "no convergió")
