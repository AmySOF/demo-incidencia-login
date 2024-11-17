import logging
from db import consultar

log = logging.getLogger("AuthService")

def login(con, username, password):
    try:
        fila = consultar(con, "SELECT password FROM users WHERE lower(username) = lower(?)", (username,))
    except Exception as e:
        log.error("Error validating user token: %s", e)
        return 401, "Error: credenciales no válidas. Inténtelo nuevamente."
    if fila and fila[0] == password:
        return 200, "Bienvenido"
    return 401, "Error: credenciales no válidas. Inténtelo nuevamente."
