idades = []
try:
    nova_idade = int(input("Digite a idade para cadastro: "))
    if nova_idade < 0:
        raise ValueError("idade negativa não permitido: ")
    idades.append(nova_idade)
    print("Cadastrado com sucesso!")
except ValueError as erro:
    print(f"Entrada Invalida:{erro}")
