valor = float(input())
valor = round(valor,2)

notas = (100.00, 50.00, 20.00, 10.00, 5.00, 2.00)
moedas = (1.00, 0.50, 0.25, 0.10, 0.05, 0.01)

d_n = []
d_m = []

for n in range(len(notas)):
    d_n.append(int(valor/notas[n]))
    valor = round(valor % notas[n],2)
for m in range(len(moedas)):
    d_m.append(int(valor/moedas[m]))
    valor = round(valor % moedas[m],2)


print("NOTAS:")
for n in range(len(notas)):
    print(str(d_n[n]) + " nota(s) de R$ " + "{:.2f}".format(notas[n]))

print("MOEDAS:")
for m in range(len(moedas)):
    print(str(d_m[m]) + " moeda(s) de R$ " + "{:.2f}".format(moedas[m]))