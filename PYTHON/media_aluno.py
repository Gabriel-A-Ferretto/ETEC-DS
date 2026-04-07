aprovado = 0
media = 0
exame = 0
reprovado = 0
total = 0


for i in range(1, 7):
    nota1 = float(input(f'Digite a nota 1 do aluno {i}: '))
    nota2 = float(input(f'Digite a nota 2 do aluno {i}: '))
    media = (nota1 + nota2) / 2
    print('')
    if media <= 3:
        reprovado += 1
    elif media > 3 and media <= 7:
        exame += 1
    elif media > 7:
        aprovado += 1

    total += media

mediaclasse = total/i

print('Total de alunos reprovados:', reprovado)
print('Total de alunos com exame: ', exame)
print('Total alunos aprovados: ', aprovado)

print('A media da classe: ', mediaclasse)

