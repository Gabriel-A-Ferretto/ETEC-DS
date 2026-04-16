
alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    idade = input("Digite a idade do aluno: ")
    
    
    idade = int(idade)
    
    
    aluno = {"nome": nome, "idade": idade}
    
    
    alunos.append(aluno)


print("\nAlunos cadastrados:")
for a in alunos:
    print(f"Nome: {a['nome']}, Idade: {a['idade']}")


if len(alunos) > 0:
    soma_idades = 0
    for a in alunos:
        soma_idades += a['idade']
    media_idade = soma_idades / len(alunos)
    print(f"\nMédia das idades: {media_idade:.2f}")

    
    mais_velho = alunos[0]
    for a in alunos:
        if a['idade'] > mais_velho['idade']:
            mais_velho = a
    print(f"Aluno mais velho: {mais_velho['nome']} com {mais_velho['idade']} anos")
else:
    print("Nenhum aluno cadastrado.")
