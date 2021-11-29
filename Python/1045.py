lados_triangulo = [float(x) for x in input().split()]
lista_lados = [0, 1, 2]
triangulo = True

A = max(lados_triangulo)
lado_maior = lados_triangulo.index(A)
lista_lados.remove(lado_maior)

C = min(lados_triangulo)
if A != C:
    lado_menor = lados_triangulo.index(C)
    lista_lados.remove(lado_menor)

    B = lados_triangulo[lista_lados[0]]

else:
    B = A

if A >= B + C:
    print("NAO FORMA TRIANGULO")
    triangulo = False
if triangulo == True:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 >= (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    elif A**2 <= (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B == C):
        print("TRIANGULO ISOSCELES")

