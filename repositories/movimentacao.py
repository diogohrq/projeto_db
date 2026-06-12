from db.connection import get_connection
from models.movimentacao import Movimentacao

class MovimentacaoRepo:
  def buscar_todos(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, id_produto, tipo, quantidade, data FROM movimentacao")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Movimentacao(row[0], row[1], row[2], row[3], row[4]) for row in rows]

  def buscar_por_id(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, id_produto, tipo, quantidade, data FROM movimentacao WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return Movimentacao(row[0], row[1], row[2]) if row else None

  def inserir(self, movimentacao):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO movimentacao (id, id_produto, tipo, quantidade, data) VALUES (%s, %s, %s, %s, %s)",
      (movimentacao.id, movimentacao.id_produto, movimentacao.tipo, movimentacao.quantidade, movimentacao.data)
    )
    conn.commit()
    cursor.close()
    conn.close()
  
  def deletar(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movimentacao WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()