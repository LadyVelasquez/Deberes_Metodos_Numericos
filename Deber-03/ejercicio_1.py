def cortar_3_decimales(x: float) -> float:
    return int(x * 1000) / 1000

suma_directa = 0.0
for i in range(1, 11):         
    termino = 1 / (i * i)
    suma_directa += termino
    suma_directa = cortar_3_decimales(suma_directa)

suma_inversa = 0.0
for i in range(10, 0, -1):     
    termino = 1 / (i * i)
    suma_inversa += termino
    suma_inversa = cortar_3_decimales(suma_inversa)

print("Parte (a)")
print("  Suma:", suma_directa)
print("  Suma inversa", suma_inversa)

suma_directa = 0.0
for i in range(1, 11):
    termino = 1 / (i * i * i)
    suma_directa += termino
    suma_directa = cortar_3_decimales(suma_directa)

suma_inversa = 0.0
for i in range(10, 0, -1):
    termino = 1 / (i * i * i)
    suma_inversa += termino
    suma_inversa = cortar_3_decimales(suma_inversa)

print("\nParte (b)")
print("  Suma:", suma_directa)
print("  Suma inversa:", suma_inversa)
