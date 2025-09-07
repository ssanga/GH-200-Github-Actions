"""
Tests unitarios para la calculadora
"""

import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """Clase de tests para la calculadora"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.calc = Calculadora()
    
    def test_sumar(self):
        """Test para la función sumar"""
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)
        self.assertEqual(self.calc.sumar(-5, -3), -8)
    
    def test_restar(self):
        """Test para la función restar"""
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(1, 1), 0)
        self.assertEqual(self.calc.restar(-2, -5), 3)
        self.assertEqual(self.calc.restar(0, 5), -5)
    
    def test_multiplicar(self):
        """Test para la función multiplicar"""
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)
        self.assertEqual(self.calc.multiplicar(-4, -5), 20)
    
    def test_dividir(self):
        """Test para la función dividir"""
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(9, 3), 3)
        self.assertEqual(self.calc.dividir(-8, 2), -4)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.3333333333333333)
    
    def test_dividir_por_cero(self):
        """Test para verificar que dividir por cero lanza excepción"""
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
    
    def test_potencia(self):
        """Test para la función potencia"""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(3, 2), 9)
        self.assertEqual(self.calc.potencia(-2, 2), 4)
    
    def test_raiz_cuadrada(self):
        """Test para la función raíz cuadrada"""
        self.assertEqual(self.calc.raiz_cuadrada(4), 2)
        self.assertEqual(self.calc.raiz_cuadrada(9), 3)
        self.assertEqual(self.calc.raiz_cuadrada(0), 0)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), 1.4142135623730951)
    
    def test_raiz_cuadrada_numero_negativo(self):
        """Test para verificar que la raíz cuadrada de número negativo lanza excepción"""
        with self.assertRaises(ValueError):
            self.calc.raiz_cuadrada(-4)


if __name__ == "__main__":
    unittest.main()