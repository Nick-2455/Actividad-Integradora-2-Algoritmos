import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import resolver_problema2

class TestProblema2(unittest.TestCase):
    def test_resolver_problema2_1(self):
        archivo_entrada = r'data/inputsProblema2/inputProblema2_1.txt'
        distancia, ruta = resolver_problema2(archivo_entrada)

        self.assertEqual(len(ruta), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)