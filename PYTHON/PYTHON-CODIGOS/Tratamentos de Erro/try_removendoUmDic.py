estoque = {"mouse": 10, "teclado": 5}
item = "monitor"
try:
    del estoque[item]
except KeyError:
    print(f"Avso: O item {item} não existe no estoque")
finally:
    print("Busca no estoque finalizada.")