from models.produto import Produto
from models.categoria import Categoria
from models.marca import Marca
from controllers.produto_controller import ProdutoController
from controllers.estoque_controller import EstoqueController
from repositories.categoria_repo import CategoriaRepo
from repositories.marca_repo import MarcaRepo

produto_ctrl = ProdutoController()
estoque_ctrl = EstoqueController()
categoria_repo = CategoriaRepo()
marca_repo = MarcaRepo()

print("\n===== CATEGORIAS =====")
for c in categoria_repo.buscar_todos():
    print(f"{c.id} - {c.nome}")

print("\n===== MARCAS =====")
for m in marca_repo.buscar_todos():
    print(f"{m.id} - {m.nome}")

print("\n===== PRODUTOS =====")
for p in produto_ctrl.listar_produtos():
    print(f"{p.id} - {p.nome} - R${p.preco}")

print("\n===== CADASTRANDO NOVO PRODUTO =====")
novo = Produto(21, "Sabão em Pó 1kg", 12.90, 4, 3)
produto_ctrl.cadastrar_produto(novo, 21)

print("\n===== REGISTRANDO ENTRADA =====")
estoque_ctrl.registrar_entrada(21, 21, 50)

print("\n===== REGISTRANDO SAIDA =====")
estoque_ctrl.registrar_saida(22, 21, 10)

print("\n===== CONSULTANDO ESTOQUE =====")
estoque = estoque_ctrl.consultar_estoque(21)
print(f"Produto 11 - Quantidade em estoque: {estoque.quantidade}")