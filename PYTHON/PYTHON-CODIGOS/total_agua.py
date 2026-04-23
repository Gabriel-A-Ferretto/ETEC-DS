total_ml = 0


for i in range(1, 8):
    quantidade = float(input(f"Digite a quantidade de agua (em ml) no momento {i}: "))
    total_ml += quantidade

total_litros = total_ml / 1000

print(f"\nTotal consumido: {total_litros:.2f} litros")

if total_litros < 2:
    print("ALERTA: Consumo de agua abaixo do recomendado!")
else:
    print("Consumo de agua adequado!")