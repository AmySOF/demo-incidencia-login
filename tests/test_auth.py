import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from db import conectar, crear_indice
from auth import login

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.con = conectar(); crear_indice(cls.con)
    def test_credenciales_validas(self):
        self.assertEqual(login(self.con, "jgarcia", "clave123")[0], 200)
    def test_clave_incorrecta(self):
        self.assertEqual(login(self.con, "jgarcia", "mala")[0], 401)
    def test_usuario_inexistente(self):
        self.assertEqual(login(self.con, "nadie", "x")[0], 401)
    def test_timeout_devuelve_503(self):
        con = conectar(limite_s=0.0)   # sin indice y limite 0 => timeout
        self.assertEqual(login(con, "jgarcia", "clave123")[0], 503)

if __name__ == "__main__":
    unittest.main()
