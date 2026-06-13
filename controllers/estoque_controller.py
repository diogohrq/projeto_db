from repositories.estoque_repo import EstoqueRepo
from repositories.movimentacao_repo import MovimentacaoRepo
from models.movimentacao import Movimentacao

class EstoqueController:
  def __init__(self):
    self.estoque_repo = EstoqueRepo()
    self.movimentacao_repo = MovimentacaoRepo()

  def consultar_estoque(self, id_produto):
    estoque = self.estoque_repo.buscar_por_id_produto(id_produto)
    if not estoque:
      print("Produto não encontrado no estoque.")
      return None
    return estoque

  def registrar_entrada(self, id, id_produto, quantidade):
    estoque = self.estoque_repo.buscar_por_id_produto(id_produto)
    if not estoque:
      print("Produto não encontrado no estoque.")
      return

    estoque.quantidade += quantidade
    self.estoque_repo.atualizar(estoque)

    mov = Movimentacao(id, id_produto, "ENTRADA", quantidade)
    self.movimentacao_repo.inserir(mov)
    print(f"Entrada de {quantidade} unidades registrada com sucesso.")

  def registrar_saida(self, id, id_produto, quantidade):
    estoque = self.estoque_repo.buscar_por_id_produto(id_produto)
    if not estoque:
      print("Produto não encontrado no estoque.")
      return

    if estoque.quantidade < quantidade:
      print(f"Estoque insuficiente. Disponível: {estoque.quantidade}")
      return

    estoque.quantidade -= quantidade
    self.estoque_repo.atualizar(estoque)

    mov = Movimentacao(id, id_produto, "SAIDA", quantidade)
    self.movimentacao_repo.inserir(mov)
    print(f"Saída de {quantidade} unidades registrada com sucesso.")