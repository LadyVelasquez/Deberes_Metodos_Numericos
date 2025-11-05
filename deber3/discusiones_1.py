def suma_inversa(valores):
    s = 0.0
    for i in range(len(valores) - 1, -1, -1):
        s += valores[i]
    return s

datos = [1.0, 2.0, 3.0, 4.0]
resultado = suma_inversa(datos)
print("Datos:", datos)
print("Suma en orden inverso:", resultado)
