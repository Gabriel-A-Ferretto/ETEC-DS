preco = [100, 250, 0, 400]
for p in preco:
    try:
      desconto = 10 / p
      print(f"Resultado: {desconto}")
    except ZeroDivisionError:
     print("Erro não possivel dividir por Zero")