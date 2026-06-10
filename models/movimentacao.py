from datetime import datetime

class Movimentacao:
  def __init__(self, id, produto_id, tipo, quantidade, data):
    self.id = id
    self.produto_id = produto_id
    self.tipo = tipo
    self.quantidade = quantidade
    self.data = data or datetime.now()