entrada = input()
entrada = entrada.split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])

nope = 0
if not (B>C):
    nope = 1
if not (D>A):
    nope = 1
if not (C+D)>(A+B):
    nope = 1
if not C>0:
    nope = 1
if not D>0:
    nope = 1
if not (A%2 == 0):
    nope = 1

if nope == 1:
    print("Valores nao aceitos")
else:
    print("Valores aceitos")