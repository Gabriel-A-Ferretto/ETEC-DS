class ControleEstoque:
    def __init__(self, produto, quantidade):
      self.produto = produto
      self.quantidade = quantidade
    def dar_baixa(self, qtd_saida):
      try:
        if qtd_saida > self.quantidade:
          raise ValueError("Estoque insuficiente!")

        self.quantidade -= qtd_saida
        print(f"Baixa realizada! Restam {self.quantidade} unidades de {self.produto}.")

      except ValueError as e:
        print(f"Erro no Estoque: {e}")

item = ControleEstoque("Teclado Mecânico", 10)

item.dar_baixa(7)