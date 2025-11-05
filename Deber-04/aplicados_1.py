import math

L = 10.0     
r = 1.0      
V_obj = 12.4 

def f(h):
    return L * (0.5 * math.pi * r**2
                - r**2 * math.asin(h / r)
                - h * math.sqrt(r**2 - h**2)) - V_obj

def biseccion(a, b, TOL, N0):
    i = 1
    FA = f(a)
    while i <= N0:
        p = a + (b - a)/2
        FP = f(p)
        if FP == 0 or (b - a)/2 < TOL:
            return p
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return None

h = biseccion(0.0, 1.0, 0.01, 100)   
print("Profundidad del agua h ≈", round(h, 2), "cm")
