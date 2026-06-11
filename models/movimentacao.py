from datetime import datetime

class Movimentacao:
  def __init__(self, id, id_produto, tipo, quantidade, data):
    self.id = id
    self.id_produto = id_produto
    self.tipo = tipo
    self.quantidade = quantidade
    self.data = data or datetime.now()