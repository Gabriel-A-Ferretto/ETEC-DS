class Aluno:
    def __init__(self, nome, modulo, curso):
        self.nome = nome
        self.modulo = modulo
        self.curso = curso

    def exibir_dados(self):
        print(f"Aluno: {self.nome} | Módulo: {self.modulo} | Curso: {self.curso}")

turma = [
    Aluno("Ana Silva", 1, "Desenvolvimento de Sistemas"),
    Aluno("Carlos Oliveira", 2, "Informática para Internet"),
    Aluno("Jorge Albuquerque",3, "Computação Forence"),
    Aluno("Paulo Souza", 1, "Seurança da Informação"),
    Aluno("Elvis Ferretto",2, "Redes de Computador")
]

for a in turma:
    a.exibir_dados()