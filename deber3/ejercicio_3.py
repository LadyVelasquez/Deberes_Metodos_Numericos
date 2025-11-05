import math

tolerancia = 1e-3
x1 = 1/5
x2 = 1/239

n = 0
while True:
    n += 1
    t1 = (x1 ** (2*n + 1)) / (2*n + 1)
    t2 = (x2 ** (2*n + 1)) / (2*n + 1)
    error = 16 * t1 + 4 * t2
    if error < tolerancia:
        break

print("Número de términos necesarios:", n)
