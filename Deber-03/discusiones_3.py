def suma_serie(x=0.25, tol=1e-6):
    rhs = (1 + 2 * x) / (1 + x + x * x)
    lhs = 0.0
    k = 1
    while True:
        num = (2 ** (k - 1)) * (x ** (2 ** (k - 1) - 1)) - (2 ** k) * (x ** (2 ** k - 1))
        if k == 1:
            den = 1 - x + x ** 2
        elif k == 2:
            den = 1 - x + x ** 4
        else:
            den = 1 - x ** (2 ** (k - 1)) + x ** (2 ** k)
        term = num / den
        lhs += term
        if abs(lhs - rhs) < tol:
            return k, lhs, rhs
        k += 1

n_terms, lhs_val, rhs_val = suma_serie()
print("Número de términos usados:", n_terms)
print("Lado izquierdo:", lhs_val)
print("Lado derecho:", rhs_val)
print("Diferencia:", abs(lhs_val - rhs_val))
