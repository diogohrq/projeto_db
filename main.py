from models.categoria import Categoria
from repositories.categoria_repo import CategoriaRepo
from repositories.produto_repo import ProdutoRepo

repo = ProdutoRepo()
produtos = repo.buscar_todos()

for c in produtos:
  print(f"{c.id} - {c.nome} - {c.preco} - {c.id_categoria} - {c.id_marca}")