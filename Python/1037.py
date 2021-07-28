numero = round(float(input()),5)


Intervalos = [[0,25],[25,50],[50,75],[75,100]]

if numero < 0 or 100 < numero:
        print("Fora do intervalo")
else:
    for ni in Intervalos:
        if ni[0] == 0:
            if round(ni[0],4) <= numero <= round(ni[1],4):
                print("Intervalo [0,25]")
        elif round(ni[0],4) < numero <= round(ni[1],4):
            print("Intervalo (" + str(ni[0]) + "," + str(ni[1]) + "]")
        