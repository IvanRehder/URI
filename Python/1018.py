valor = int(input())

n_100 = int(valor/100)
valor_rest = valor % 100

n_50 = int(valor_rest/50)
valor_rest = valor_rest % 50

n_20 = int(valor_rest/20)
valor_rest = valor_rest % 20

n_10 = int(valor_rest/10)
valor_rest = valor_rest % 10

n_5 = int(valor_rest/5)
valor_rest = valor_rest % 5

n_2 = int(valor_rest/2)
valor_rest = valor_rest % 2

n_1 = int(valor_rest/1)

print(str(valor))
print(str(n_100) + " nota(s) de R$ 100,00")
print(str(n_50) + " nota(s) de R$ 50,00")
print(str(n_20) + " nota(s) de R$ 20,00")
print(str(n_10) + " nota(s) de R$ 10,00")
print(str(n_5) + " nota(s) de R$ 5,00")
print(str(n_2) + " nota(s) de R$ 2,00")
print(str(n_1) + " nota(s) de R$ 1,00")