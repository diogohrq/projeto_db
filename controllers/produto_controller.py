from repositories.produto_repo import ProdutoRepo
from repositories.estoque_repo import EstoqueRepo
from models.estoque import Estoque

class ProdutoController:
  def __init__(self):
    self.produto_repo = ProdutoRepo()
    self.estoque_repo = EstoqueRepo()

  def listar_produtos(self):
    produtos = self.produto_repo.buscar_todos()
    if not produtos:
      print("Nenhum produto cadastrado.")
      return []
    return produtos

  def buscar_produto(self, id):
    produto = self.produto_repo.buscar_por_id(id)
    if not produto:
      print("Produto não encontrado.")
      return None
    return produto

  def cadastrar_produto(self, produto, id_estoque):
    self.produto_repo.inserir(produto)
    estoque = Estoque(id_estoque, produto.id, 0)
    self.estoque_repo.inserir(estoque)
    print(f"Produto '{produto.nome}' cadastrado com estoque zerado.")

  def atualizar_produto(self, produto):
    self.produto_repo.atualizar(produto)
    print(f"Produto '{produto.nome}' atualizado com sucesso.")

  def deletar_produto(self, id):
    self.produto_repo.deletar(id)
    print(f"Produto deletado com sucesso.")