import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import problema2

class TestProblema2(unittest.TestCase):
    def test_resolver_problema2_1(self):
        archivo_entrada = r'../data/inputsProblema1/inputProblema1.txt'
        ruta, distancia = problema2.tsp_main(archivo_entrada)

        self.assertEqual(len(ruta), 6)
    
    def test_resolver_problema2_2(self):
        archivo_entrada = r'../data/inputsProblema1/inputProblema1_Caso2.txt'
        ruta, distancia = problema2.tsp_main(archivo_entrada)

        self.assertEqual(distancia, 0)
    
    def test_resolver_problema2_3(self):
        archivo_entrada = r'../data/inputsProblema1/inputProblema1_Caso3.txt'
        ruta, distancia = problema2.tsp_main(archivo_entrada)

        self.assertEqual(len(ruta), 3)
    
    def test_resolver_problema2_4(self):
        archivo_entrada = r'../data/inputsProblema1/inputProblema1_Caso4.txt'
        ruta, distancia = problema2.tsp_main(archivo_entrada)

        self.assertEqual(len(ruta), 2)
    
    def test_resolver_problema2_5(self):
        archivo_entrada = r'../data/inputsProblema1/inputProblema1_Caso5.txt'
        ruta, distancia = problema2.tsp_main(archivo_entrada)

        self.assertEqual(distancia, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)