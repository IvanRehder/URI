#numeros = input()
numeros = input().split()

N1 = int(numeros[0])
N2 = int(numeros[1])

if N1 >= N2:
    resto = N1 % N2
else:
    resto = N2 % N1

if resto == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
