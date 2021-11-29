comeco_fim = [int(x) for x  in input().split()]

comeco = comeco_fim[0]
fim = comeco_fim[1]

if comeco < fim:
    duracao = fim - comeco
else:
    duracao = fim + 24 - comeco

print("O JOGO DUROU {} HORA(S)".format(duracao))