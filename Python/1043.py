pontos = input()
pontos = pontos.split()

A = float(pontos[0])
B = float(pontos[1])
C = float(pontos[2])

if  A < B + C and \
    B < A + C and \
    C < A + B:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = (A + B)*C/2
    print("Area = {:.1f}".format(area))

print()
print("TESTE IVAN {:00004.2f}".format(10))