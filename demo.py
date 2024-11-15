import logging, time
from db import conectar
from auth import login
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
con = conectar()
if __name__ == "__main__":
    t = time.time()
    codigo, msg = login(con, "jgarcia", "clave123")   # credenciales CORRECTAS
    print(f"HTTP {codigo} | {msg} | {time.time()-t:.3f}s")
