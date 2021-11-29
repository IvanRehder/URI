comeco_fim = [int(x) for x  in input().split()]

comeco_hora = comeco_fim[0]
comeco_minuto = comeco_fim[1]
fim_hora = comeco_fim[2]
fim_minuto = comeco_fim[3]

comeco_minuto_total = comeco_hora*60 + comeco_minuto
fim_minuto_total = fim_hora*60 + fim_minuto

if comeco_minuto_total < fim_minuto_total:
    duracao = fim_minuto_total - comeco_minuto_total
else:
    duracao = fim_minuto_total + 24*60 - comeco_minuto_total

print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(int(duracao/60), duracao % 60))