from datetime import date

class Movimentacao:
  def __init__(self, id, id_produto, tipo, quantidade, data):
    self.id = id
    self.id_produto = id_produto
    self.tipo = tipo.upper()
    self.quantidade = quantidade
    self.data = data or date.today()