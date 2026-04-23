matriz_dados =[[10, 20], [30, "erro"]]
soma = 0
try:
    for linha in matriz_dados:
        for item in linha:
            soma += item
except TypeError as e:
    print(f"Erro de processamento na matriz: {e}")
    