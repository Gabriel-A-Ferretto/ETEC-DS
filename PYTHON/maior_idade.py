somaIdade = 0
maior = 0
media = 0

for x  in range(1,7):
    idade = int(input(f'Digite a idade: {x} '))
    if idade >= 18:
        maior += 1

    somaIdade +=  idade
media = somaIdade / x


print(f'Quantidade de pessoas com mais de 18 anos {maior}')
print(f'Media da idades{media}')
