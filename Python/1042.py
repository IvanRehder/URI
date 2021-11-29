numeros = input()
numeros = numeros.split()

N1 = int(numeros[0])
N2 = int(numeros[1])
N3 = int(numeros[2])

if N1 > N2:
    if N1 > N3:
        maior = N1
        if N2 > N3:
            meio = N2
            menor = N3
        else:
            meio = N3
            menor = N2
    else:
        maior = N3
        meio = N1
        menor = N2
else:
    if  N2 > N3:
        maior = N2
        if N1 > N3:
            meio = N1
            menor = N3
        else:
            meio = N3
            menor = N1
    else:
        maior = N3
        meio = N2
        menor = N1

print(menor)
print(meio)
print(maior)
print()
print(N1)
print(N2)
print(N3)