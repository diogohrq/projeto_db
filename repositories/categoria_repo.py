from db.connection import get_connection
from models.categoria import Categoria

class CategoriaRepo:
  def buscar_todos(self):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM categoria")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [Categoria(row[0], row[1]) for row in rows]

  def buscar_por_id(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM categoria WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return Categoria(row[0], row[1]) if row else None
     
  def inserir(self, categoria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (id, nome) VALUES (%s, %s)", (categoria.id, categoria.nome))
    conn.commit()
    cursor.close()
    conn.close()
  
  def atualizar(self, categoria):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE categoria SET nome = %s WHERE id = %s", (categoria.nome, categoria.id))
    conn.commit()
    cursor.close()
    conn.close()
  
  def deletar(self, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    


    