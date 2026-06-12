from db.connection import get_connection
from models.produto import Produto

class ProdutoRepo:
  def buscar_todos(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, id_categoria, id_marca FROM produto")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Produto(row[0], row[1], row[2], row[3], row[4]) for row in rows]

  def buscar_por_id(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, id_categoria, id_marca FROM produto WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return Produto(row[0], row[1]) if row else None
     
  def inserir(self, produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO produto (id, nome, preco, id_categoria, id_marca) VALUES (%s, %s, %s, %s, %s)", 
      (produto.id, produto.nome, produto.preco, produto.id_categoria, produto.id_marca)
    )
    conn.commit()
    cursor.close()
    conn.close()
  
  def atualizar(self, produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "UPDATE produto SET nome = %s, preco = %s, id_categoria = %s, id_marca = %s WHERE id = %s",
      (produto.nome, produto.preco, produto.id_categoria, produto.id_marca, produto.id)
    )
    conn.commit()
    cursor.close()
    conn.close()
  
  def deletar(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produto WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()