alunos = {"123": "Ana", "456": "Carlos"}
try:
    matricula = input("Digite a matricula: ")
    print(f"Aluno: {alunos[matricula]}")
except KeyError:
    print(f"Erro A matricula {matricula} não foi encontrada")