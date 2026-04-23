usuarios = []
def ccadastrar_senha():
    try:
        senha = input("Crie uma senha (minmo 6 caracteres): ")
        if len(senha) < 6:
            raise ValueError("A seguranaça exige pelo menos 6 caracteres")
        usuarios.append(senha)
        print("Senha cadastrada com sucesso!")
    except ValueError as erro:
        print(f"Erro de Validação: {erro}")
ccadastrar_senha()