import cmath

def raices_estables(a, b, c):
    D = b * b - 4 * a * c
    r = cmath.sqrt(D)
    if b >= 0:
        q = -0.5 * (b + r)
    else:
        q = -0.5 * (b - r)
    x1 = q / a
    x2 = c / q
    return x1, x2

a, b, c = 1.0, -3.0, 2.0
x1, x2 = raices_estables(a, b, c)
print("Coeficientes:", a, b, c)
print("Raíz 1:", x1)
print("Raíz 2:", x2)
