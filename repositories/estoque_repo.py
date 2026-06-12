from db.connection import get_connection
from models.estoque import Estoque

class EstoqueRepo:
  def buscar_todos(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, id_produto, quantidade FROM estoque")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Estoque(row[0], row[1], row[2]) for row in rows]

  def buscar_por_id(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, id_produto, quantidade FROM estoque WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return Estoque(row[0], row[1], row[2]) if row else None

  def inserir(self, estoque):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO estoque (id, id_produto, quantidade) VALUES (%s, %s, %s)",
      (estoque.id, estoque.id_produto, estoque.quantidade)
    )
    conn.commit()
    cursor.close()
    conn.close()
  
  def atualizar(self, estoque):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE estoque SET id_produto = %s, quantidade = %s WHERE id = %s", (estoque.id_produto, estoque.quantidade, estoque.id))
    conn.commit()
    cursor.close()
    conn.close()
  
  def deletar(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estoque WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
