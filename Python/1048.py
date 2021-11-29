salario = float((input()))

if (0 < salario <= 400):
    taxa = 15
elif (400 < salario <= 800):
    taxa = 12
elif (800 < salario <= 1200):
    taxa = 10
elif (1200 < salario <= 2000):
    taxa = 7
elif (2000 < salario):
    taxa = 4

aumento = salario * taxa/100
novo_salario = salario + aumento

print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(aumento))
print('Em percentual: {} %'.format(taxa))
