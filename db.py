import sqlite3, time

class QueryTimeout(Exception):
    pass

class Conexion(sqlite3.Connection):
    limite = 0.02

def conectar(n_usuarios=300_000, limite_s=0.02):
    """BD en memoria con usuarios. limite_s simula el timeout de consulta."""
    con = sqlite3.connect(":memory:", factory=Conexion)
    con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    con.executemany("INSERT INTO users(username,password) VALUES (?,?)",
                    ((f"user{i}", "clave123") for i in range(n_usuarios)))
    con.execute("INSERT INTO users(username,password) VALUES ('jgarcia','clave123')")
    con.commit()
    con.limite = limite_s
    return con

def consultar(con, sql, params=()):
    inicio = time.time()
    def vigilar():
        return 1 if time.time() - inicio > con.limite else 0
    con.set_progress_handler(vigilar, 1000)
    try:
        return con.execute(sql, params).fetchone()
    except sqlite3.OperationalError:
        raise QueryTimeout('Timeout while querying table "users"')
    finally:
        con.set_progress_handler(None, 0)

def crear_indice(con):
    con.execute("CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)")
