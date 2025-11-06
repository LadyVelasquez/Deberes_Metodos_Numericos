from scipy.optimize import newton
import math

#Ejercicio 1
def fprime(x):
    return -3*x**2 + math.sin(x)

p1 = newton(func = lambda x : -x**3 - math.cos(x), x0 = -1, fprime = fprime)
print(p1)
p2 = newton(func = lambda x : -x**3 - math.cos(x), x0 = -1)
print(p2)

#Ejercicio2
pa = newton(func = lambda x : x**3 - 2*x**2 - 5, x0 = 1, tol = 10e-4, x1 = 4)
print(pa)
pb = newton(func = lambda x : x**3 + 3*x**2 - 1, x0 = -3, tol = 10e-4, x1 = -2)
print(pb)
pc = newton(func = lambda x : x - math.cos(x), x0 = 0, tol = 10e-4, x1 = math.pi/2)
print(pc)
pd = newton(func = lambda x : x - 0.8 - 0.2*math.sin(x), x0 = 0, tol = 10e-4, x1 = math.pi/2)
print(pd)


#Ejercicio 3
p1 = newton(func = lambda x : 3*x - math.exp(x), x0 = 1,
           fprime = lambda x : 3 - math.exp(x), tol = 10e-5, x1 = 2)
print(p1)

p1 = newton(func = lambda x : 3*x - math.exp(x), x0 = 1, tol = 10e-5, x1 = 2)
print(p1)

p1 = newton(func = lambda x : 2*x + 3*math.cos(x) - math.exp(x),
            x0 = 1,
           fprime = lambda x : 2 - 3*math.sin(x) - math.exp(x),
            tol = 10e-5, x1 = 2)
print(p1)

p1 = newton(func = lambda x : 2*x + 3*math.cos(x) - math.exp(x), 
            x0 = 1, tol = 10e-5, x1 = 2)
print(p1)

#Ejercicio 4

#Método de la Secante
p1 = newton(func = lambda x : 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9, 
            x0 = -1, tol = 10e-6, x1 = 0)
print(p1)

p1 = newton(func = lambda x : 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9, 
            x0 = 1, tol = 10e-6)
print(p1)

#Método de Newton
p1 = newton(func = lambda x : 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9,
            x0 = -0.5,
           fprime = lambda x : 920*x**3 + 54*x**2 + 18*x -221,
            tol = 10e-6)
print(p1)

p1 = newton(func = lambda x : 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9,
            x0 = 1,
           fprime = lambda x : 920*x**3 + 54*x**2 + 18*x -221,
            tol = 10e-6)
print(p1)

from scipy.optimize import newton, bisect
import math
def f_5(x):
    return math.tan(math.pi * x) - 6
def df_5(x):
    return math.pi / (math.cos(math.pi * x)**2)

# a. Método de Bisección
res_5a = bisect(f_5, 0, 0.48, maxiter=10, full_output=True, disp=False)
print(f"a) Bisección: Raíz = {res_5a[0]}, Iteraciones = {res_5a[1].iterations}")

# b. Método de Newton
res_5b = newton(func=f_5, x0=0, fprime=df_5, maxiter=10, 
                full_output=True, disp=False)
print(f"b) Newton: Raíz = {res_5b[0]}, Iteraciones = {res_5b[1].iterations}, Convergió: {res_5b[1].converged}")
# c. Método de la Secante
res_5c = newton(func=f_5, x0=0, x1=0.48, maxiter=10, 
                full_output=True, disp=False)
print(f"c) Secante: Raíz = {res_5c[0]}, Iteraciones = {res_5c[1].iterations}, Convergió: {res_5c[1].converged}")

p1 = newton(func = lambda x : math.log(x**2 + 1) - math.exp(0.4*x)*math.cos(math.pi*x),
            x0 = 24.5, tol = 10e-6)
print(p1)

from scipy.optimize import newton
import math
def f_7(x):
    if x >= 0:
        return x**(1/3)
    else:
        return -(-x)**(1/3)

def df_7(x):
    if x == 0:
        return float('inf')
    return 1 / (3 * (f_7(x)**2))

# a) Método de Newton
res_7a = newton(f_7, x0=1, fprime=df_7, maxiter=10, 
                full_output=True, disp=False)
print(f"a) Newton: Raíz = {res_7a[0]}, Iteraciones = {res_7a[1].iterations}, Convergió: {res_7a[1].converged}")

# b) Método de la Secante
res_7b = newton(f_7, x0=1, x1=0.5, maxiter=10, 
                full_output=True, disp=False)
print(f"b) Secante: Raíz = {res_7b[0]}, Iteraciones = {res_7b[1].iterations}, Convergió: {res_7b[1].converged}")