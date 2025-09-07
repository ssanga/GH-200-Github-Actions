"""
Calculadora simple para pruebas de GitHub Actions
"""

class Calculadora:
    """Clase calculadora con operaciones básicas"""
    
    def sumar(self, a, b):
        """Suma dos números"""
        return a + b
    
    def restar(self, a, b):
        """Resta dos números"""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplica dos números"""
        return a * b
    
    def dividir(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        return base ** exponente
    
    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return numero ** 0.5

    def nothing(self, numero):
        return numero


def main():
    """Función principal para demostrar el uso de la calculadora"""
    calc = Calculadora()
    
    print("=== Calculadora de Prueba ===")
    print(f"5 + 3 = {calc.sumar(5, 3)}")
    print(f"10 - 4 = {calc.restar(10, 4)}")
    print(f"6 * 7 = {calc.multiplicar(6, 7)}")
    print(f"15 / 3 = {calc.dividir(15, 3)}")
    print(f"2^8 = {calc.potencia(2, 8)}")
    print(f"√16 = {calc.raiz_cuadrada(16)}")


if __name__ == "__main__":
    main()