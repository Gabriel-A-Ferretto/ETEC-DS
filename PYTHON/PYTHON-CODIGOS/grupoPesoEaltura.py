
maior_altura = 0
menor_altura = float('informação: ')
soma_mulheres = 0
cont_mulheres = 0
cont_homens = 0
sexo_mais_alto = ""


for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    # Verifica maior e menor altura
    if altura > maior_altura:
        maior_altura = altura
        sexo_mais_alto = sexo

    if altura < menor_altura:
        menor_altura = altura

    # Contagem e soma
    if sexo == 'F':
        soma_mulheres += altura
        cont_mulheres += 1
    elif sexo == 'M':
        cont_homens += 1

# Média das mulheres
if cont_mulheres > 0:
    media_mulheres = soma_mulheres / cont_mulheres
else:
    media_mulheres = 0

# Resultados
print(f"Maior altura: {maior_altura}")
print(f"Menor altura: {menor_altura}")
print(f"Média de altura das mulheres: {media_mulheres:.2f}")
print(f"Número de homens: {cont_homens}")
print(f"Sexo da pessoa mais alta: {sexo_mais_alto}")