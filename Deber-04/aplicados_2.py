import math

s0 = 300.0      
m = 0.25        
k = 0.1         
g = 9.81

def s(t):
    return s0 - (m*g/k)*t + (m*m*g)/(k*k) * (1 - math.exp(-k*t/m))

def f(t):
    return s(t) - 0.0   

def biseccion(f, a, b, TOL, N0):
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

t_impacto = biseccion(f, 0.0, 30.0, 0.01, 1000)
print("Tiempo de impacto ≈", round(t_impacto, 2), "s")
