from db.connection import get_connection
from models.marca import Marca

class MarcaRepo:
  def buscar_todos(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM marca")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Marca(row[0], row[1]) for row in rows]

  def buscar_por_id(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM marca WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return Marca(row[0], row[1]) if row else None
     
  def inserir(self, marca):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO marca (id, nome) VALUES (%s, %s)", (marca.id, marca.nome))
    conn.commit()
    cursor.close()
    conn.close()
  
  def atualizar(self, marca):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE marca SET nome = %s WHERE id = %s", (marca.nome, marca.id))
    conn.commit()
    cursor.close()
    conn.close()
  
  def deletar(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM marca WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()