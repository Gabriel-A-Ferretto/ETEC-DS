numeros = [10, 20, 30]
try:
    pos = int(input("Digite a posição para ver o dobro: "))
    print(f"Resultado: {numeros[pos] * 2}")
except ValueError:
    print("Erro: Digite um número inteiro.")
except IndexError:
    print("Erro: Posição inexistente na lista.")