matriz = [[0,0], [0,0]]
try:
    valor = int(input("Digital um número inteiro para a posição [0][0]: "))
    matriz[0][0] = valor
    print(matriz)
except ValueError:
    print("Erro: Digite apenas números inteiros validos.")
    