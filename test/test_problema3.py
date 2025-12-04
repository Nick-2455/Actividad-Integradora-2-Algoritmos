import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import resolver_problema3

class TestProblema3(unittest.TestCase):

    def test_resolver_problema3(self):
        archivo_entrada = r'data/inputsProblema3/inputProblema3.txt'
        
        flujo_max = resolver_problema3(archivo_entrada)

        self.assertEqual(flujo_max, 23)

    def test_resolver_problema3_Caso2(self):
        archivo_entrada = r'data/inputsProblema3/inputProblema3_Caso2.txt'
        
        flujo_max = resolver_problema3(archivo_entrada)

        self.assertEqual(flujo_max, 10)

    def test_resolver_problema3_Caso3(self):
        archivo_entrada = r'data/inputsProblema3/inputProblema3_Caso3.txt'
        
        flujo_max = resolver_problema3(archivo_entrada)

        self.assertEqual(flujo_max, 0)

    def test_resolver_problema3_Caso4(self):
        archivo_entrada = r'data/inputsProblema3/inputProblema3_Caso4.txt'
        
        flujo_max = resolver_problema3(archivo_entrada)

        self.assertEqual(flujo_max, 5)

    def test_resolver_problema3_Caso5(self):
        archivo_entrada = r'data/inputsProblema3/inputProblema3_Caso5.txt'
        
        flujo_max = resolver_problema3(archivo_entrada)

        self.assertEqual(flujo_max, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)