cordenadas = (10, 20, 30)
try:
    indice = int(input("Qual coordenada acessa (0, 1 ou 2) ?"))
    print(f"Valor {cordenadas[indice]}")
except IndexError:
    print("Erro: O indicce iformado está fora do intervalo da tupla.")

