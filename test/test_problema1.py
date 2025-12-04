import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import resolver_problema1

class TestProblema1(unittest.TestCase):
    def test_resolver_problema1(self):
        archivo_entrada = r'data/inputsProblema1/inputProblema1.txt'
        
        totalCosto, aristasMST = resolver_problema1(archivo_entrada)
        
        self.assertEqual(totalCosto, 16)

        self.assertEqual(len(aristasMST), 4)

    def test_resolver_problema1_Caso2(self):
        archivo_entrada = r'data/inputsProblema1/inputProblema1_Caso2.txt'
        
        totalCosto, aristasMST = resolver_problema1(archivo_entrada)
        
        self.assertEqual(totalCosto, 5)

        self.assertEqual(len(aristasMST), 3)

    def test_resolver_problema1_Caso3(self):
        archivo_entrada = r'data/inputsProblema1/inputProblema1_Caso3.txt'
        
        totalCosto, aristasMST = resolver_problema1(archivo_entrada)
        
        self.assertEqual(totalCosto, 4)

        self.assertEqual(len(aristasMST), 1)

    def test_resolver_problema1_Caso4(self):
        archivo_entrada = r'data/inputsProblema1/inputProblema1_Caso4.txt'
        
        totalCosto, aristasMST = resolver_problema1(archivo_entrada)
        
        self.assertEqual(totalCosto, 0)

        self.assertEqual(len(aristasMST), 0)

    def test_resolver_problema1_Caso5(self):
        archivo_entrada = r'data/inputsProblema1/inputProblema1_Caso5.txt'
        
        totalCosto, aristasMST = resolver_problema1(archivo_entrada)

        self.assertEqual(totalCosto, 0)

        self.assertEqual(len(aristasMST), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)