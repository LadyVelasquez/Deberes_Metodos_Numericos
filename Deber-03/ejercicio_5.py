def suma_original(a, b):
    n = len(a)
    S = 0.0
    for i in range(n):
        for j in range(i + 1):
            S += a[i] * b[j]
    return S

def suma_optimizada(a, b):
    n = len(a)
    # prefijos de b
    c = [0.0] * n
    c[0] = b[0]
    for i in range(1, n):
        c[i] = c[i-1] + b[i]
    # suma final
    S = 0.0
    for i in range(n):
        S += a[i] * c[i]
    return S
