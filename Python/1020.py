dias = int(input())

ano = int(dias/365)
dias_rest = dias % 365
mes = int(dias_rest/30)
dia = dias_rest % 30

print(str(ano) + " ano(s)")
print(str(mes) + " mes(s)")
print(str(dia) + " dia(s)")