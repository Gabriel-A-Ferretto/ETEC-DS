pessoas = 1
mediaAltura = 0
numeroMulheres = 0
numeroHomens = 0
alturaMulheres = 0


while pessoas <= 5:
    altura = float(input(f'Digite a altura da pessoa: {pessoas}' ))
    sexo = input(f'Digite o sexo da pessoa: {pessoas}')
    if sexo.upper() == 'M':
        numeroMulheres += 1
    else:
        alturaMulheres += altura
        numeroMulheres += 1
    pessoas += 1

print(f'Media das Mulheres: {alturaMulheres/numeroMulheres}')
print(f'Numero de homens: {numeroHomens}')
