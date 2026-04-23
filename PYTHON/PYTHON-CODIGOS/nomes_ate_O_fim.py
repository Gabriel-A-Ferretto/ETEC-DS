nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    
    if nome.lower() == "fim":
        break
    
    nomes.append(nome)

# Mostrando todos os nomes
print("\nNomes digitados:")
for n in nomes:
    print(n)

# Quantidade total de nomes
print(f"\nQuantidade de nomes digitados: {len(nomes)}")

# Quantidade de nomes com mais de 5 letras
contador = 0
for n in nomes:
    if len(n) > 5:
        contador += 1

print(f"Quantidade de nomes com mais de 5 letras: {contador}")
