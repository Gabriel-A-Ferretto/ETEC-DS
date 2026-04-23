fruta = ["maça", "banana", "uva"]
while True: 
 try:
    busca = input("Digite o valor pra busca: (fim para sarr)")
    if busca != "fim":
        indice = fruta.index(busca)
        print("a posição: ", indice)
    else:
        break
 except ValueError:
    print(f"A fruta {busca} não esta na lista")