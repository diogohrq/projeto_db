from db.connection import get_connection

conn = get_connection()
print("Conexão bem sucedida!" if conn.is_connected() else "Falhou.")
conn.close()