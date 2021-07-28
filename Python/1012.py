input = input()
input = input.split()

A = float(input[0])
B = float(input[1])
C = float(input[2])

area_ta = A*C/2
area_ci = 3.14159*C**2
area_tz = (A+B)*C/2
area_qu = B**2
area_re = A*B

print("TRIANGULO: " + "{:.3F}".format(area_ta))
print("CIRCULO: " + "{:.3F}".format(area_ci))
print("TRAPEZIO: " + "{:.3F}".format(area_tz))
print("QUADRADO: " + "{:.3F}".format(area_qu))
print("RETANGULO: " + "{:.3F}".format(area_re))