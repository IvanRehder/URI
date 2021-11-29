notas = input()
notas = notas.split()

N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])

W1 = 2
W2 = 3
W3 = 4
W4 = 1

media = (N1 * W1 + N2 * W2 + N3 * W3 + N4 * W4)/(W1 + W2 + W3 + W4)

print("Media: {:.1f}".format(media))

if media > 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    mediaFinal = (media + notaExame)/2
    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(mediaFinal))
