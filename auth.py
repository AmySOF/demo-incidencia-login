import logging
from db import consultar, QueryTimeout

log = logging.getLogger("AuthService")

def login(con, username, password):
    try:
        fila = consultar(con, "SELECT password FROM users WHERE username = ?", (username,))
    except QueryTimeout:
        log.error("DB timeout en login (sin datos sensibles)")
        return 503, "Servicio temporalmente no disponible. Intente en unos minutos."
    if fila and fila[0] == password:
        return 200, "Bienvenido"
    return 401, "Error: credenciales no válidas. Inténtelo nuevamente."
