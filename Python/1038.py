entrada = input()
entrada = entrada.split()

X = float(entrada[0])
Y = float(entrada[1])

tabelaPreco = [[1, 4.00],[2, 4.50],[3, 5.00],[4, 2.00], [5, 1.50]]

for item in tabelaPreco:
    if item[0] == X:
        print("Total: R$ {0:.2f}".format(item[1]*Y))